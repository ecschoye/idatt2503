#include <iomanip>
#include <iostream>
#include <openssl/evp.h>
#include <openssl/sha.h>
#include <sstream>
#include <string>

std::string hex(const std::string &input) {
    std::stringstream hex_stream;
    hex_stream << std::hex << std::internal << std::setfill('0');
    for (auto &byte : input)
        hex_stream << std::setw(2) << (int)(unsigned char)byte;
    return hex_stream.str();
}

std::string pbkdf2(const std::string &password, const std::string &salt, int iterations) noexcept {
    const auto hash_length = SHA_DIGEST_LENGTH;

    std::string hash(SHA_DIGEST_LENGTH, '\0');

    PKCS5_PBKDF2_HMAC(
            password.c_str(), password.size(),
            reinterpret_cast<const unsigned char *>(salt.c_str()), salt.size(),
            iterations,
            EVP_sha1(),
            hash_length, reinterpret_cast<unsigned char *>(&hash[0])
    );

    return hash;
}

static int counter = 0;

void check_password_combination(const std::string& alphabets, std::string& current_combination, const std::string& salt, const std::string& known_hash, int max_depth) {
    counter++;

    if (counter % 1000000 == 0) {
        std::cout << "Combination so far: " << current_combination << std::endl;
        counter = 0;
    }

    if (current_combination.size() > max_depth) {
        return;
    }

    std::string hash = pbkdf2(current_combination, salt, 2048);
    if (hex(hash) == known_hash) {
        std::cout << "Password found: " << current_combination << std::endl;
        exit(0);
    }

    for (char c : alphabets) {
        current_combination.push_back(c);
        check_password_combination(alphabets, current_combination, salt, known_hash, max_depth);
        current_combination.pop_back();
    }
}



int main() {
    std::string alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    std::string key = "ab29d7b5c589e18b52261ecba1d3a7e7cbf212c6";
    std::string salt = "Saltet til Ola";
    std::string current_combination;
    int max_depth = 3;

    check_password_combination(alphabets, current_combination, salt, key, max_depth);


}
