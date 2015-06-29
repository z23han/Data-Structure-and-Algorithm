import java.util.*;

public class SuffixTreeNode {
	HashMap<Character, SuffixTreeNode> children = new HashMap<Character, SuffixTreeNode>();
	char value;
	ArrayList<Integer> indexes = new ArrayList<Integer>();

	public SuffixTreeNode() {}

	public void insertString(String s, int index) {
		indexes.add(index);
		if (s != null && s.length() > 0) {
			// check the first character in s
			value = s.charAt(0);
			SuffixTreeNode child = null;
			// check if HashMap children has this value as key
			if (children.containsKey(value)) {
				child = children.get(value);
			} else {
				// if not, we create a new Node and assign to children
				child = new SuffixTreeNode();
				children.put(value, child);
			}
			String remainder = s.substring(1);
			// continue to test the remainder
			child.insertString(remainder, index);
		}
	}

	public ArrayList<Integer> getIndexes(String s) {
		// when we recurse to the end, we return the total indexes
		if (s == null || s.length() == 0) {
			return indexes;
		} else {
			char first = s.charAt(0);
			if (children.containsKey(first)) {
				String remainder = s.substring(1);
				return children.get(first).getIndexes(remainder);
			}
		}
		return null;
	}
}