
import java.util.*;
public class TestCollections {
	public static void main(String args[]) {
		ArrayList<String>list=new ArrayList<String>();
		list.add("Raviu");
		list.add("Vijay");
		list.add("Ajith");
		list.add("Siva");
		Iterator itr=list.iterator();
		while(itr.hasNext()) {
			System.out.println(itr.next());
		}
	}

}
