mod pass;
mod scope;

use ast::*;

pub fn run(ast: &mut Program) {
    scope::pass(ast);
}

#[cfg(test)]
mod tests {
    use super::*;
    use parser::parse_script;
    use std::error::Error;

    #[test]
    fn it_works() -> Result<(), Box<Error>> {
        let parse_result = parse_script("wau")?;
        run(&mut ast::Program::Script(*parse_result));
        Ok(())
    }
}