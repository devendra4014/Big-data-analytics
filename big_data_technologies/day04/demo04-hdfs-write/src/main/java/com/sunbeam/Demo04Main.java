package com.sunbeam;

import java.io.PrintStream;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hdfs.DistributedFileSystem;

public class Demo04Main {
	public static void main(String[] args) {
		Configuration conf = new Configuration();
		conf.set("fs.defaultFS", "hdfs://localhost:9000");
		try(DistributedFileSystem dfs = (DistributedFileSystem) FileSystem.get(conf)) {
			String filePath = "/user/nilesh/file2.txt";
			Path path = new Path(filePath);
			try(FSDataOutputStream dout = dfs.create(path)) {
				try(PrintStream out = new PrintStream(dout)) {
					out.println("This is a new file created using Java API....");
					out.println("Data is uploaded using FsDataOutputStream....");
					out.println("Can flush the data to hadoop at the end....");
					//dout.flush(); // send data in memory over network to datanode.
					//dout.hflush(); // send data in memory over network to datanode -- in its memory -- ack by datanode.
					dout.hsync(); // send data in memory over network to datanode -- in its memory and then written on datanode disk -- ack by datanode
				} // out.close();
			} // dout.close(); // --> internally calls dout.flush();
		} // dfs.close();
		catch (Exception e) {
			e.printStackTrace();
		}
		System.out.println("File written on HDFS.");
	}
}
