/**
 * RMIT AppSec Compliance Hub
 * Main JavaScript - MD Rendering & Navigation
 */

// Simple Markdown to HTML converter
const md = {
    render: function(text) {
        let html = text;

        // Escape HTML
        html = html.replace(/</g, '&lt;').replace(/>/g, '&gt;');

        // Headers
        html = html.replace(/^### (.*$)/gm, '<h3>$1</h3>');
        html = html.replace(/^## (.*$)/gm, '<h2>$1</h2>');
        html = html.replace(/^# (.*$)/gm, '<h1>$1</h1>');

        // Bold and italic
        html = html.replace(/\*\*\*(.*?)\*\*\*/g, '<strong><em>$1</em></strong>');
        html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');

        // Code blocks
        html = html.replace(/```(\w*)\n([\s\S]*?)```/g, '<pre><code class="language-$1">$2</code></pre>');
        html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

        // Tables
        html = html.replace(/^\|(.+)\|$/gm, function(match, content) {
            const cells = content.split('|').map(c => c.trim());
            if (cells.every(c => /^[-:]+$/.test(c))) {
                return '<!--table-separator-->';
            }
            return '<tr>' + cells.map(c => '<td>' + c + '</td>').join('') + '</tr>';
        });
        html = html.replace(/((<tr>.*<\/tr>\n?)+)/g, function(match) {
            const rows = match.replace(/<!--table-separator-->\n?/g, '');
            const firstRow = rows.match(/<tr>(.*?)<\/tr>/);
            if (firstRow) {
                const header = firstRow[0].replace(/<td>/g, '<th>').replace(/<\/td>/g, '</th>');
                const body = rows.replace(firstRow[0], '').trim();
                return '<table class="md-table"><thead>' + header + '</thead><tbody>' + body + '</tbody></table>';
            }
            return '<table class="md-table">' + rows + '</table>';
        });

        // Blockquotes
        html = html.replace(/^&gt; (.*$)/gm, '<blockquote>$1</blockquote>');
        html = html.replace(/<\/blockquote>\n<blockquote>/g, '\n');

        // Horizontal rules
        html = html.replace(/^---$/gm, '<hr>');

        // Links
        html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank">$1</a>');

        // Lists
        html = html.replace(/^\- (.*$)/gm, '<li>$1</li>');
        html = html.replace(/^\d+\. (.*$)/gm, '<li>$1</li>');
        html = html.replace(/(<li>.*<\/li>\n?)+/g, function(match) {
            return '<ul>' + match + '</ul>';
        });

        // Paragraphs
        html = html.replace(/\n\n/g, '</p><p>');
        html = '<p>' + html + '</p>';

        // Clean up empty paragraphs
        html = html.replace(/<p>\s*<\/p>/g, '');
        html = html.replace(/<p>\s*(<h[1-6]>)/g, '$1');
        html = html.replace(/(<\/h[1-6]>)\s*<\/p>/g, '$1');
        html = html.replace(/<p>\s*(<table)/g, '$1');
        html = html.replace(/(<\/table>)\s*<\/p>/g, '$1');
        html = html.replace(/<p>\s*(<ul>)/g, '$1');
        html = html.replace(/(<\/ul>)\s*<\/p>/g, '$1');
        html = html.replace(/<p>\s*(<pre>)/g, '$1');
        html = html.replace(/(<\/pre>)\s*<\/p>/g, '$1');
        html = html.replace(/<p>\s*(<hr>)/g, '$1');
        html = html.replace(/(<hr>)\s*<\/p>/g, '$1');
        html = html.replace(/<p>\s*(<blockquote>)/g, '$1');
        html = html.replace(/(<\/blockquote>)\s*<\/p>/g, '$1');

        return html;
    }
};

// Load and render markdown file
async function loadMarkdown(mdPath, targetId) {
    const target = document.getElementById(targetId);
    if (!target) return;

    try {
        target.innerHTML = '<div class="loading">Loading content...</div>';
        const response = await fetch(mdPath);
        if (!response.ok) throw new Error('Failed to load ' + mdPath);
        const text = await response.text();
        target.innerHTML = md.render(text);
        target.classList.add('md-content');
    } catch (error) {
        target.innerHTML = '<div class="error">Error loading content: ' + error.message + '</div>';
        console.error(error);
    }
}

// Get base path for navigation
function getBasePath() {
    const path = window.location.pathname;
    if (path.includes('/pages/')) {
        return '../';
    }
    return './';
}

// Initialize navigation highlighting
function initNavigation() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.header-nav a, .sidebar-nav a').forEach(link => {
        const href = link.getAttribute('href');
        if (href && (href.endsWith(currentPage) || (currentPage === 'index.html' && href === './'))) {
            link.classList.add('active');
        }
    });
}

// Document ready
document.addEventListener('DOMContentLoaded', function() {
    initNavigation();

    // Load MD content if data-md attribute exists
    document.querySelectorAll('[data-md]').forEach(el => {
        const mdPath = el.getAttribute('data-md');
        loadMarkdown(mdPath, el.id);
    });
});
