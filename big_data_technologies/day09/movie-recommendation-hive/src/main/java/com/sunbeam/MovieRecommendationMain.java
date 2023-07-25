package com.sunbeam;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.Scanner;

public class MovieRecommendationMain {
	public static final String DB_DRIVER = "org.apache.hive.jdbc.HiveDriver";
	public static final String DB_URL = "jdbc:hive2://localhost:10000/dbda";
	public static final String DB_USER = "nilesh";
	public static final String DB_PASSWORD = "";

	static {
	    try {
	        // load and register jdbc driver
	        Class.forName(DB_DRIVER);
	    } catch(Exception ex) {
	        ex.printStackTrace();
	        System.exit(1);
	    }
	}

	public static void main(String[] args) {
	    // Input movie id from user
	    Scanner sc = new Scanner(System.in);
	    System.out.print("Enter a movie id: ");
	    int movieId = sc.nextInt();
	    // create connection
	    try(Connection con = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
	        String sql = "SELECT m.id, m.title, mc.cnt, mc.cor FROM movies_orc m INNER JOIN movies_corr mc ON (mc.m1 = m.id OR mc.m2 = m.id) WHERE mc.cor IS NOT NULL AND mc.cnt > 50 AND (mc.m1 = ? OR mc.m2 = ?) AND (m.id != ?) ORDER BY mc.cor DESC LIMIT 5";
	        // create statement
	        try(PreparedStatement stmt = con.prepareStatement(sql)) {
	            // set parameters
	            stmt.setInt(1, movieId);
	            stmt.setInt(2, movieId);
	            stmt.setInt(3, movieId);
	            // execute query
	            try(ResultSet rs = stmt.executeQuery()) {
	                // process result
	                while(rs.next()) {
	                    int id = rs.getInt(1);
	                    String title = rs.getString(2);
	                    double cor = rs.getDouble(4);
	                    int cnt = rs.getInt(3);
	                    System.out.printf("%d, %s, %.2f, %d\n", id, title, cor, cnt);
	                }
	            } // rs.close();
	        } // stmt.close();
	    } // con.close();
	    catch(Exception ex) {
	        ex.printStackTrace();
	    }
	}

}
