fn escape_html(s: &str) -> String {
    s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
}

fn main() {
    println!("Enter string: ");
    let mut input = String::new();
    match std::io::stdin().read_line(&mut input) {
        Ok(_) => {
            let line = input.trim_end().to_string();
            let escaped_line = escape_html(&line);
            println!("{}", escaped_line);
        }
        Err(error) => println!("error: {}", error),
    }
}
