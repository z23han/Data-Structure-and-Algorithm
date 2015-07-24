import java.util.*;

public class Trie {
	protected final Map<Character, Trie=""> children;
	protected String value;
	protected boolean isWord = false;

	private Trie(String value) {
		this.value = value;
		children = new HashMap<Character, Trie="">();
	}

	public Trie() {
		this("");
	}

	public void add(String word) {
		if (word == null || word.length() == 0) {
			System.out.println("Cannot add null or empty string!");
			return;
		}
		Trie node = this;
		for (Char c : word.toCharArray()) {
			if (!node.children.containsKey(c)) {
				node.put(c);
			}
			node = node.children.get(c);
		}
		isWord = true;
	}

	private void put(Char c) {
		children.put(c, new Trie(this.value+c));
	}

	public boolean contains(String s) {
		Trie node = this;
		for (Char c : s.toCharArray()) {
			if (!node.children.containsKey(c)) {
				return false;
			}
			node = node.children.get(c);
		}
		return node.value.equals(s);
	}
}