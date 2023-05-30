#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

vector<tuple<int, int, int>> three_sum(vector<int> array, int target)
{
	// Create a table to store all the possible pairs of numbers that sum to a given value.
	vector<vector<int>> table(array.size() + 1);
	for (int i = 0; i < array.size(); i++)
	{
		for (int j = i + 1; j < array.size(); j++)
		{
			table[array[i] + array[j]].push_back(i);
			table[array[i] + array[j]].push_back(j);
		}
	}

	// Iterate over all the possible triplets.
	vector<tuple<int, int, int>> triplets;
	for (int i = 0; i < array.size(); i++)
	{
		for (int j = i + 1; j < array.size(); j++)
		{
			for (int k = j + 1; k < array.size(); k++)
			{
				if (array[i] + array[j] + array[k] == target)
				{
					triplets.push_back(make_tuple(array[i], array[j], array[k]));
				}
			}
		}
	}

	return triplets;
}

int main()
{
	vector<int> array = {-1, 0, 1, 2, -1, -4};
	int target = 0;

	vector<tuple<int, int, int>> triplets = three_sum(array, target);

	for (auto triplet : triplets)
	{
		cout << get(triplet) << ", " << get(triplet) << ", " << get(triplet) << endl;
	}

	return 0;
}
