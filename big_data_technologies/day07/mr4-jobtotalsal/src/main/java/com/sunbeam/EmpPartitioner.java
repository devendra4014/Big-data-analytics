package com.sunbeam;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Partitioner;

public class EmpPartitioner extends Partitioner<Text, DoubleWritable> {
	@Override
	public int getPartition(Text key, DoubleWritable value, int numPartitions) {
		//HashPartitioner Internals: return key.hashCode() % numPartitions;
		String job = key.toString();
		if(job.equals("CLERK") || job.equals("MANAGER") || job.equals("PRESIDENT"))
			return 0; // partition 0
		else
			return 1; // partition 1
	}
}
