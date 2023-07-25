package com.sunbeam;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.LocatedFileStatus;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.RemoteIterator;
import org.apache.hadoop.hdfs.DistributedFileSystem;

public class Demo03Main {
	public static void main(String[] args) {
		String dirPath = "/user/nilesh";
		Configuration conf = new Configuration();
		conf.set("fs.defaultFS", "hdfs://localhost:9000");
		try(DistributedFileSystem dfs = (DistributedFileSystem) FileSystem.get(conf)) {
			Path path = new Path(dirPath);
			FileStatus[] files = dfs.listStatus(path);
			for(FileStatus file:files) {
				System.out.println("Name: " + file.getPath().getName());
				System.out.println("Size: " + file.getLen());
				System.out.println("Replication: " + file.getReplication());
				System.out.println("Block size: " + (int)(file.getBlockSize()/1024.0/1024.0));
				System.out.println("User/Group: " + file.getOwner() + "/" + file.getGroup());
				System.out.println();
			}
		} // dfs.close();
		catch (Exception e) {
			e.printStackTrace();
		}
	}
}
