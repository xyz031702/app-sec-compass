// SpotBugsDemo.java
//
// Compile:  javac SpotBugsDemo.java
// Run SpotBugs (after compiling):  spotbugs -textui -effort:max -high .
//-------------------------------------------------------------

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.Map;

public class SpotBugsDemo {

    private int[] secretNumbers = {42, 7, 13};      // URF_UNREAD_FIELD, EI_EXPOSE_REP
    private String unused = "dead field";           // URF_UNREAD_FIELD

    /** Exposes internal mutable array — SpotBugs: EI_EXPOSE_REP */
    public int[] getSecretNumbers() {
        return secretNumbers;
    }

    /** Null‑pointer dereference on some paths — SpotBugs: NP_NULL_PARAM_DEREF */
    public void printLength(String text) {
        if (text == null) {
            // forgot to return or substitute a default
        }
        System.out.println("Length = " + text.length());
    }

    /** Builds a query by concatenation — SpotBugs: SQL_INJECTION_JDBC */
    public void unsafeQuery(String user) throws SQLException {
        Connection conn = DriverManager.getConnection("jdbc:h2:mem:test");
        Statement  st   = conn.createStatement();
        String sql      = "SELECT * FROM users WHERE username = '" + user + "'";
        ResultSet rs    = st.executeQuery(sql);
        while (rs.next()) {
            System.out.println(rs.getString(1));
        }
        st.close();
        conn.close();
    }

    /** Dead store — SpotBugs: DLS_DEAD_LOCAL_STORE */
    public void deadStoreExample() {
        int tmp = 0;
        tmp = 123; // never used again
    }

    /** Wrong iterator over Map — SpotBugs: WMI_WRONG_MAP_ITERATOR */
    public void wrongIterator(Map<String,String> map) {
        for (String key : map.keySet()) {
            Map.Entry<String,String> e = map.entrySet().iterator().next();
            System.out.println(key + " = " + e.getValue());
        }
    }

    /** Equals implementation with unrelated type logic — SpotBugs: EC_UNRELATED_TYPES */
    @Override
    public boolean equals(Object obj) {
        if (obj instanceof String) {   // incompatible operand
            return true;
        }
        return super.equals(obj);
    }

    public static void main(String[] args) throws Exception {
        SpotBugsDemo demo = new SpotBugsDemo();

        demo.printLength(null);                      // triggers NPE at runtime
        demo.unsafeQuery(args.length > 0 ? args[0] : "admin");
        System.out.println(java.util.Arrays.toString(demo.getSecretNumbers()));
        demo.deadStoreExample();

        HashMap<String,String> m = new HashMap<>();
        m.put("a", "1");
        demo.wrongIterator(m);
    }
}
