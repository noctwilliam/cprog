import java.util.*;
class sorting{
	public static int[] quicksort(int[] arr) {
		if (arr.length <= 1) {
			return arr;
		}
		int pivot = arr[arr.length / 2];
		ArrayList<Integer> left = new ArrayList<Integer>();
		ArrayList<Integer> middle = new ArrayList<Integer>();
		ArrayList<Integer> right = new ArrayList<Integer>();
		for (int i : arr) {
			if (i < pivot) {
				left.add(i);
			} else if (i == pivot) {
				middle.add(i);
			} else {
				right.add(i);
			}
		}
		int[] result = new int[arr.length];
		int i = 0;
		for (int x : quicksort(toIntArray(left))) {
			result[i++] = x;
		}
		for (int x : middle) {
			result[i++] = x;
		}
		for (int x : quicksort(toIntArray(right))) {
			result[i++] = x;
		}
		return result;
	}

	public static int[] toIntArray(ArrayList<Integer> list) {
		int[] ret = new int[list.size()];
		for (int i = 0; i < ret.length; i++) {
			ret[i] = list.get(i).intValue();
		}
		return ret;
	}

	public static void main(String[] args) {
		int arr [] = {1,2,9,3,8,12};
		int sortedArr [] = quicksort(arr);
		// print before sorted
		for(int i = 0; i < arr.length; i++){
			System.out.println(arr[i]);
		}
		for(int i = 0; i < sortedArr.length; i++){
			System.out.println(sortedArr[i]);
		}
	}
}