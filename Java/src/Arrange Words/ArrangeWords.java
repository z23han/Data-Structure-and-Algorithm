// 2 dictionaries, the first one stores all prefix (single L)
// the second one stores all first and second prefixes (double L). 

import java.util.*;

public class ArrangeWords {
	public static List<String> arrangeWords(Set<String> dicts) {
		if (dicts == null || dicts.size() == 0) {
			throw new IllegalArgumentException("Invalid input!");
		}
		Map<String, Integer> singleL = new HashMap<String, Integer>();
		Map<String, Integer> doubleL = new HashMap<String, Integer>();
		// singleL and doubleL are dictionaries mapping the letter(s) to the frequencies. 
		for (String s : dicts) {
			if (!singleL.containsKey(s.substring(0, 1))) {
				singleL.put(s.substring(0, 1), 1);
			} else {
				// frequencies++
				singleL.put(s.substring(0, 1), singleL.get(s.substring(0, 1))+1);
			}

			if (!doubleL.containsKey(s.substring(0, 2))) {
				doubleL.put(s.substring(0, 2), 1);
			} else {
				// frequencies++
				doubleL.put(s.substring(0, 2), doubleL.get(s.substring(0, 2))+1);
			}
		}

		Map<String, Integer> words = new HashMap<String, Integer>();
		List<String> rst = new ArrayList<String>();
		boolean found = false;
		// outer loops
		for (String s1 : dicts) {
			for (int i = 0; i < 3; i++) {
				String tmp = s1.substring(i, i+1);
				if (!isValid(tmp, words, singleL)) {
					continue;
				}
			}
			rst.add(s1);
			// inner loops
			for (String s2 : dicts) {
				if (s2.equals(s1)) {
					continue;
				}
				for (int i = 0; i < 3; i++) {
					String tmp = s1.substring(i, i+1) + s2.substring(i, i+1);
					if (!isValid(tmp, words, doubleL)) {
						continue;
					}
				}
				String d1 = s1.substring(0, 1) + s2.substring(1, 2);
				if (!isValid(d1, words, doubleL)) {
					continue;
				}
				String d2 = s1.substring(2, 3) + s2.substring(1, 2);
				if (!isValid(d2, words, doubleL)) {
					continue;
				}
				rst.add(s2);
				for (String s3 : dicts) {
					if (s3.equals(s1) || s3.equals(s2)) {
						continue;
					}
					for (int i = 0; i < 3; i++) {
						String tmp = s1.substring(i, i+1) + s2.substring(i, i+1) + s3;
						if (!dicts.contains(tmp)) {
							continue;
						}
					}
					String dia1 = s1.substring(0, 1) + s2.substring(1, 2) + s3.substring(2, 3);
					String dia2 = s1.substring(2, 3) + s2.substring(1, 2) + s3.substring(0, 1);
					if (!dicts.contains(dia1) || !dicts.contains(dia2)) {
						continue;
					}
					found = true;
					rst.add(s3);
					break;
				}
				if (found) {
					break;
				}
				rst.remove(s2);
			}
			if (found) {
				break;
			}
			rst.remove(s1);
		}
		if (rst.size() < 3) {
			return new ArrayList<String>();
		}
		return rst;
	}


	// used for checking word is in both words and prefixes
	// making sure that the frequencies of word in words shouldn't bigger than that in prefixes
	private static boolean isValid(String word, 
		Map<String, Integer>words, Map<String, Integer>prefixes) {
		if (!prefixes.containsKey(word)) {
			return false;
		}
		if (!words.containsKey(word)) {
			words.put(word, 1);
		} else {
			words.put(word, words.get(word)+1);
		}
		//System.out.println(words);

		if (words.get(word) > prefixes.get(word)) {
			return false;
		}
		return true;
	}

	public static void main(String[] args) {
		Set<String> dicts = new HashSet<String>();
		dicts.add("abc");
		dicts.add("def");
		dicts.add("ghi");
		dicts.add("adg");
		dicts.add("beh");
		dicts.add("cfi");
		dicts.add("aei");
		dicts.add("ceg");
		dicts.add("acg");
		dicts.add("dgh");
		dicts.add("iok");
		dicts.add("pkm");
		System.out.println(dicts);

		for (String s : arrangeWords(dicts)) {
			System.out.println(s);
		}
	}
}

