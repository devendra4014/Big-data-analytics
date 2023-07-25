package com.sunbeam;

import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class EmpReducer extends Reducer<Text, DoubleWritable, Text, DoubleWritable> {
	private DoubleWritable totalSalWr = new DoubleWritable();
	@Override
	protected void reduce(Text key, Iterable<DoubleWritable> values,
			Reducer<Text, DoubleWritable, Text, DoubleWritable>.Context context) throws IOException, InterruptedException {
		double total = 0.0;
		for(DoubleWritable salWr:values) {
			double sal = salWr.get();
			total = total + sal;
		}
		totalSalWr.set(total);
		context.write(key, totalSalWr);
	}
}
