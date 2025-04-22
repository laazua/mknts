package env

import (
    "github.com/joho/godotenv"
)

func Load() {
    // load default .env file
    err := godotenv.Load()
    if err != nil {
        panic(err)
    }
}
