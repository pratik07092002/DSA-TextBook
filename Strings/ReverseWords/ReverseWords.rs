fn reverse_words(s: String)-> String {
    s.split_whitespace().rev().collect::<Vec<&str>>().join(" ")
}

fn main(){
let input = String::from("Hello World");
let answer = reverse_words(input);
println!("Answer is this {answer}");
}