package com.sunbeam.dbda;

import java.util.Scanner;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hdfs.DistributedFileSystem;

public class Demo01Main {
	public static void main(String[] args) {
		Configuration conf = new Configuration();
		conf.set("fs.defaultFS", "hdfs://localhost:9000");
		try(DistributedFileSystem dfs = (DistributedFileSystem)FileSystem.get(conf)) {
			Path filePath = new Path("/user/nilesh/welcome.txt");
			try(FSDataInputStream din = dfs.open(filePath )) {
				try(Scanner sc = new Scanner(din)) {
					while(sc.hasNextLine()) {
						String line = sc.nextLine();
						System.out.println(line);
					}
				} // sc.close();
			} // din.close();
		} // dfs.close();
		catch (Exception e) {
			e.printStackTrace();
		}
	}
}



