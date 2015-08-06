import java.util.*;
import java.util.stream.*;

public class MySet {
	public static void main(String[] args) {
		//distinctWords(args);
		forMethods(args);
	}

	public static void distinctWords(String[] inputWords) {
		Set<String> distWords = Arrays.asList(inputWords).stream().collect(Collectors.toSet());
		System.out.println(distWords.size() + " distinct words: " + distWords);
	}

	public static void forMethods(String[] inputWords) {
		Set<String> s = new HashSet<String>();
		for (String a : inputWords) {
			s.add(a);
			System.out.println(s.size() + " distinct words: " + s + " by forMethods.");
		}
	}
}