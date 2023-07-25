package parseCSV;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class parseCSV {
		///home/sunbeam/Documents/java_class/emp.csv
	public static void main(String[] args) {
		ArrayList<emp> arrEmp=new ArrayList<emp>();
		//File f=new File(args[0]);
		File f=new File("/home/sunbeam/Documents/java_class/emp.csv");
		try {
			Scanner sc=new Scanner(f);
			while(sc.hasNextLine())
			{
				String line=sc.nextLine();
				emp e=parseLine(line);
				if(e!=null)
					arrEmp.add(e);
//				System.out.println(line);
			}
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		 for(emp e: arrEmp)
			 System.out.println(e);
	}

		private static emp parseLine(String line) {
			
			try {
				emp e=new emp();
				String []parts=line.split(",");
				e.setId(Integer.parseInt(parts[0]));
				e.setEname(parts[1]);
				e.setJob(parts[2]);
				e.setMgr(Integer.parseInt(parts[3]));
				e.setSal(Integer.parseInt(parts[4]));
				e.setDeptno(Integer.parseInt(parts[5]));
				return e;
			} catch (NumberFormatException e) {
				//ignore code
			}
			return null;
		}

		

}
