// Convert number to reversed array of digits
// Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

// Example(Input => Output):
// 35231 => [1,3,2,5,3]
// 0 => [0]

package kata

func Digitize(n int) []int {
	if n == 0 {
		var res = []int{0}
		return res
	}
	var res []int
	for n > 0 {
		res = append(res, n%10)
		n = n / 10
	}
	return res
}
