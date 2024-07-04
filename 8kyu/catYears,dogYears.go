// I have a cat and a dog.

// I got them at the same time as kitten/puppy. That was humanYears years ago.

// Return their respective ages now as [humanYears,catYears,dogYears]

// NOTES:

// humanYears >= 1
// humanYears are whole numbers only
// Cat Years
// 15 cat years for first year
// +9 cat years for second year
// +4 cat years for each year after that
// Dog Years
// 15 dog years for first year
// +9 dog years for second year
// +5 dog years for each year after that

package kata

func CalculateYears(years int) (result [3]int) {
	var res [3]int
	catYears := 0
	dogYears := 0
	for i := 1; i <= years; i++ {
		if i == 1 {
			catYears += 15
			dogYears += 15
			continue
		}
		if i == 2 {
			catYears += 9
			dogYears += 9
			continue
		}
		catYears += 4
		dogYears += 5
	}
	res[0] = years
	res[1] = catYears
	res[2] = dogYears
	return res
}
