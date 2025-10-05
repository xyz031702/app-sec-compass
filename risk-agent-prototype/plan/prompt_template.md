# AI Model Security Analysis Plan Generator

## Context
This prompt is designed to generate a practical, focused plan for analyzing AI models for malicious code. It is based on the research documented in merged.md, which provides a comprehensive framework for detecting and mitigating malicious code in AI models.

## Prompt Template

Given a target AI model file, generate a practical, actionable plan for detecting potential malicious code based on the deep research report (merged.md). The plan should:

1. Be focused on direct, practical methods rather than complex frameworks
2. Reference appropriate tools as mentioned in the deep research report
3. Include simple, executable approaches for security checks
4. Be completable within a reasonable timeframe (4-5 days)
5. Cover the essential security aspects without unnecessary complexity

The plan should include the following phases as outlined in the deep research report:

### Phase 1: Essential Setup
- Environment setup as appropriate for the model format
- Directory structure for organizing analysis artifacts
- Model acquisition and verification

### Phase 2: Static Analysis
- Format verification based on model type
- Analysis for suspicious patterns
- Scanning based on techniques in the deep research report
- Entropy analysis as recommended in the research
- Binary analysis appropriate to the model format

### Phase 3: Dynamic Analysis
- Runtime behavior monitoring techniques from the research
- Network activity monitoring during model loading
- File access pattern analysis
- Memory operation monitoring

### Phase 4: Behavioral Testing
- Testing approaches from the deep research report
- Response analysis methods
- Unexpected behavior detection

### Phase 5: Results Analysis
- Consolidating findings according to the research framework
- Security assessment based on research criteria
- Recommendations aligned with the deep research

For each phase, include:
- Approaches aligned with the deep research report
- Implementation guidance based on the research
- Analysis methods as recommended in the research
- Approximate time required

Focus on detecting actual malicious code rather than implementing an overly complex security framework. Each component should directly contribute to identifying potential security threats in the model file, following the principles outlined in the deep research report.

## Example Use
To generate a plan for analyzing a specific model:

1. First do a quick overview of the target model file (typically placed in plan/target)
2. Identify the target model file format and characteristics
3. Review the deep research report (merged.md) for relevant techniques
4. Generate a tailored analysis plan based on the research and target characteristics
5. Execute the plan step by step, adjusting as needed based on findings

## Reflection on Previous Plan Generation
In our previous interaction, we started with a comprehensive but overly complex plan that included unnecessary implementation details. Through iteration, we simplified to focus on:

1. Essential approaches aligned with the deep research report
2. Direct, practical implementation guidance based on the research
3. A streamlined workflow that can be completed in a reasonable timeframe
4. Clear reporting of findings as recommended in the research

This approach proved more effective for the specific task of detecting malicious code in AI models without unnecessary complexity, while remaining true to the methodologies outlined in the deep research report.
