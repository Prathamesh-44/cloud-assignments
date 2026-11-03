import java.sql.*;

public class DbApp {
    public static void main(String[] args) throws Exception {
        String host = System.getenv().getOrDefault("DB_HOST", "mysql-db");
        String url = "jdbc:mysql://" + host + ":3306/?allowPublicKeyRetrieval=true&useSSL=false";
        Connection con = null;
        for (int i = 0; i < 30 && con == null; i++) {           // wait for MySQL to boot
            try { con = DriverManager.getConnection(url, "root", "root123"); }
            catch (SQLException e) { System.out.println("Waiting for MySQL..."); Thread.sleep(3000); }
        }
        if (con == null) throw new RuntimeException("MySQL not reachable");
        Statement st = con.createStatement();
        st.execute("CREATE DATABASE IF NOT EXISTS college");
        st.execute("USE college");
        st.execute("CREATE TABLE IF NOT EXISTS students(id INT, name VARCHAR(50))");
        st.execute("INSERT INTO students VALUES (1,'Asha'),(2,'Ravi')");
        ResultSet rs = st.executeQuery("SELECT * FROM students");
        while (rs.next()) System.out.println(rs.getInt(1) + " " + rs.getString(2));
        con.close();
    }
}
