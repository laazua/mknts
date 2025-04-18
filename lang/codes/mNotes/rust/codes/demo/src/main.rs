use demo::test_content;
use demo::test_file_mod;
use demo::test_file_mod::file_mod;
use demo::test_file_mod::dir_mod;

fn main(){
    test_content::test();
    file_mod::test();
    test_file_mod::test_func();
    dir_mod::test();
}
