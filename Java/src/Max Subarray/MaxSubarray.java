import java.util.*;

public class MaxSubarray {

	public int comp_max_array_sum(int[] nums) {
		int max_ending_here = 0;
		int max_so_far = 0;
		for (int i = 0; i < nums.length; i++) {
			max_ending_here = Math.max(0, max_ending_here+nums[i]);
			max_so_far = Math.max(max_so_far, max_ending_here);
		}
		return max_so_far;
	}

	public static void main(String[] args) {
		int[] numbers = {-2, 1, -3, 4, -1, 2, 6, -5, 4};
		MaxSubarray mxsub = new MaxSubarray();
		int max_so_far = mxsub.comp_max_array_sum(numbers);
		System.out.println(max_so_far);
	}
}