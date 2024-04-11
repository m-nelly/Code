// Documented Notes On C++

// Imports IO stream library.
#include <iostream>
// Imports string library.
#include <string>

using namespace std;
// A namespace is a collection of commands.
// These are required to avoid collisions between command names.

// Functions should be declared before main as a 'Forward Declaration' and
// defined after. C++ does not process whitespace; functions and procedures
// should be ended with a semi-colon.

void basics();
void variables();
void variable_types();
void user_input();
void arithmetic_and_assignment_operators();
void relational_operators();
void logical_operators();
void bitwise_operators();
void conditional_statements();
void conditional_switch();

// The execution of all C++ programs is derived from a call to the main()
// function.
int main() // Declaration
{          // Definition
	// This is the only function executed by the compiler.
	// This is the body of the function.

	// Uncomment lesson(s) desired to run.

	// Lessons:
	// basics_lesson();
	// variables_lesson();
	// variable_types_lesson();
	// user_input();
	// arithmetic_and_assignment_operators();
	// relational_operators();
	// logical_operators();
	// bitwise_operators();
	// conditional_statements();
	// conditional_switch();
}

void basics() {
	cout << "This is a test." << endl;
	// Sends "This is a test." to the console output and ends the line.
};

void variables() {
	int x = 4;
	// Assigns a value of 4 to x.

	cout << x << endl;
	// Prints 4 in the console out.

	/*
	1.Variables cannot be initialized twice.
	2.Variables cannot start with numbers.
	3.Variable names cannot contain spaces.
	4.Variable names should be descriptive.
	*/
};

void variable_types() {
	// Define variable type, name, and then value

	// Multiple variables can be defined under the same type, separate with commas

	/*
	Variable Types:
	1.Integer (int) Number w/o decimal. Gets 4 bytes of memory.
	2.Short Integer (short) Small number w/o decimal. Gets 2 bytes of memory.
	3.Floating Point Number (float) Small number w/ decimal. Gets 4 bytes of
	memory. 4.Double (double) Large number w/ decimal. Gets 8 bytes of memory.
	5.Character (char) Single Character
	6.String (string) Multiple Characters
	7.Boolean (bool) True/False, 1/0
	*/
	int a = 20;
	short b = 100;
	float c = 5.2;
	double d = 420.69;
	char e = 'a';
	string f = "HelloWorld!";
	bool g = true;
	// Unsigned variables hold only positive values.
	unsigned short h = 60000;
	// Variables can be locked with 'const'.
	const string permanent = "permanent";

	cout << a << endl;
	cout << b << endl;
	cout << c << endl;
	cout << d << endl;
	cout << e << endl;
	cout << f << endl;
	cout << g << endl;
	cout << h << endl;
	cout << permanent << endl;
};

void user_input() {
	string name;

	cout << "Enter your name: ";
	cin >> name; // Stores console input in $name.

	cout << "Your name is: " << name << endl;
};

void arithmetic_and_assignment_operators() {
	int a = 10;
	int b = 5;

	cout << a + b << endl;
	cout << a * b << endl;
	cout << a - b << endl;
	cout << a / b << endl;
	cout << a % b << endl; // Returns remainder after division.

	// Result matches the type of the input. If expecting a double, assign a
	// variable type of double.

	cout << (b += 1) << endl; // increments b by one.
	cout << (b -= 1) << endl; // decrements b by one.

	cout << b << endl;
	cout << b++ << endl; // Increments after sending to ourput.
	cout << b << endl;
	cout << ++b << endl; // Increments before sending to output.
};

void relational_operators() {
	int a = 10;
	int b = 5;

	/*
	'=' assigns values.
	'a == b' Returns true (1) when values match.
	'a != b' Returns true (1) when values do not match.
	'a > b'Returns true (1) when a is greater than b.
	'a < b'Returns true (1) when a is less than b.
	'a >= b'Returns true (1) when a is greater than or equal to b.
	'a <= b'Returns true (1) when a is less than or equal to b.
	*/

	cout << (a == b) << endl;
	cout << (a != b) << endl;
	cout << (a > b) << endl;
	cout << (a < b) << endl;
	cout << (a >= b) << endl;
	cout << (a <= b) << endl;
};

void logical_operators() {
	int a = 4;
	int b = 5;

	/*
	The && operator 'and' returns true (1) if both operations are true.
	The || operator 'or' returns true (1) if wither operation is true.
	The ! operator 'not' returns the opposite boolean for a given operation.
	*/

	cout << (a > 1 && a < b) << endl;
	cout << (a > 1 || a > b) << endl;
	cout << !(a > 5 && a > b) << endl;
};

void bitwise_operators() // Advanced - Optional
{
	// Bitwise operators are designed to work at the bit level.

	/*
	**********************************************************
	Decimal to Binary Conversion:

	Most Significant Bit - Leftmost Bit
	Least Significant Bit - Rightmost Bit

	Least_Significant_Bit = (2 ^ 0) = (1)
	Second_Significant_Bit = (2 ^ 1) = (2)
	Third_Significant_Bit = (2 ^ 2) = (4)
	...
	Eighth_Significant_Bit = (2 ^ 7) = (128)

	Formula: (2 ^ (n-1)) where n is positions from the left.

	Example: 155 -> Binary

	1. Determine significant bits.
			Add one to the highest x where (2 ^ x) < 155
			(2 ^ 7) = 128, (2 ^ 8) = 256
			(7 + 1) = 8 significant bits.

	2. Start with the most significant bit as a 1 and all others zero.
			1 0 0 0 0 0 0 0 = 128

	3. Add next most significant bit and compare total to 155
			1 1 0 0 0 0 0 0 = 192

	4. If the total is greater than 155, change the bit to a zero and
			move on to the next.
			1 0 1 0 0 0 0 0 = 140

	5. Repeat steps 4 & 5 until you reach 155.
			1 0 1 1 0 0 0 0 = 156
			1 0 1 0 1 0 0 0 = 148
			1 0 1 0 1 1 0 0 = 152
			1 0 1 0 1 1 1 0 = 154
			1 0 1 0 1 1 1 1 = 155

	Note: '^' is the XOR operator in C++ and is only used here as
				notation for exponential operation.
				This will not work in C++. Use the pow() function instead.
	**********************************************************
	*/
	/*
	Bitwise AND - &
	Bitwise OR - |
	Bitwise NOT - ~
	Bitwise XOR - ^ (XOR returns true (1) if one bit or the other is a 1, but not
	both.) Bitwise Shift Left - << Bitwise Shift Right - >>
	*/

	/*
	Returns 2

	 1 0 1 0
	 0 0 1 0
	&_______
	 0 0 1 0
	*/
	cout << (10 & 2) << endl;

	/*
	Returns 10

	 1 0 1 0
	 0 0 1 0
	|_______
	 1 0 1 0
	*/
	cout << (10 | 2) << endl;

	/*
	Returns -11 because all bits in the address space are reversed and
			the first bit in the adress space is a large, negative number.
	 1 0 1 0
	~_______
	 0 1 0 1

	*/
	cout << (~10) << endl;

	/*
	Returns 8
	 1 0 1 0
	 0 0 1 0
	^_______
	 1 0 0 0
	 */
	cout << (10 ^ 2) << endl;

	// Adds a zero bit after the least significant bit. Equivalent to (n * 2)
	cout << (2 << 1) << endl;

	// Removes the least significant bit. Equivalent to (n / 2)
	cout << (2 >> 1) << endl;
};

void conditional_statements() {
	// This lesson should be relatively straightforward.
	// If further explanation would be helpful, please comment on GitHub.
	int a, b;

	cout << "Enter a: ";
	cin >> a;

	cout << "Enter b: ";
	cin >> b;

	if (a > b) {
		cout << "a"
			<< " > "
			<< "b" << endl;
	}

	else if (a < b) {
		cout << "a"
			<< " < "
			<< "b" << endl;
	}

	else {
		cout << "a"
			<< " = "
			<< "b" << endl;
	}
}

void conditional_switch() { 
	int x = 50; 
	
	switch(x){
		case 10:
			cout << "10";
			break;
		case 50:
			cout << "50";
	}
}
