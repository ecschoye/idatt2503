fn replace_special_characters(s: String) -> String {
    let mut result = String::new();
    for c in s.chars() {
        if c == '&' {
            result.push_str("&amp;");
        } else if c == '<' {
            result.push_str("&lt;");
        } else if c == '>' {
            result.push_str("&gt;");
        } else {
            result.push(c);
        }
    }
    return result;
}

fn main() {
    println!("Enter string: ");
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let line = input.trim_end().to_string();
    println!("{}", replace_special_characters(line));
}
