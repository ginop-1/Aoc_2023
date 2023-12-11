# create template for Advent of Code (python)
# Usage: ./generate_template.sh <day>

DAY=$1

if [ -z "$DAY" ]; then
    echo "Usage: ./generate_template.sh <day>"
    exit 1
fi

touch "$DAY".py
touch "input$DAY".txt

echo "def p1(f):" >> "$DAY".py
echo "    pass" >> "$DAY".py
echo "" >> "$DAY".py
echo "def p2(f):" >> "$DAY".py
echo "    pass" >> "$DAY".py
echo "" >> "$DAY".py
echo "if __name__ == '__main__':" >> "$DAY".py
echo "    with open('inputs/input$DAY.txt') as f:" >> "$DAY".py
echo "        print(p1(f))" >> "$DAY".py

echo "Created $DAY.py and input$DAY.txt"
