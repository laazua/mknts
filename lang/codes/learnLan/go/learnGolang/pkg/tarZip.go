// 文件归档tar, zip
package main

import (
	"archive/tar"
	"archive/zip"
	"bytes"
	"fmt"
	"io"
	"log"
	"os"
)

func main() {
	// create a buffer to write our archive to.
	buf := new(bytes.Buffer)
	// create a new tar archive.
	t := tar.NewWriter(buf)

	// add some files to the archive.
	files := []struct {
		Name, Body string
	}{
		{"readme.txt", "this archive contains some text files."},
		{"test.txt", "test file"},
		{"todo.txt", "get animal handling licence."},
	}

	for _, file := range files {
		hdr := &tar.Header{
			Name: file.Name,
			Size: int64(len(file.Body)),
		}
		if err := t.WriteHeader(hdr); err != nil {
			log.Fatalln(err)
		}
		if _, err := t.Write([]byte(file.Body)); err != nil {
			log.Fatalln(err)
		}
	}

	// make sure to check the error on close
	if err := t.Close(); err != nil {
		log.Fatalln(err)
	}

	// Open the tar check the error on Close.
	r := bytes.NewReader(buf.Bytes())
	tr := tar.NewReader(r)
	for {
		hdr, err := tr.Next()
		if err == io.EOF {
			// end of tar archive
			break
		}
		if err != nil {
			log.Fatalln(err)
		}
		fmt.Printf("Contents of %s:\n", hdr.Name)
		if _, err := io.Copy(os.Stdout, tr); err != nil {
			log.Fatalln(err)
		}
		fmt.Println()
	}

	// Open a zip archive for reading
	zr, err := zip.OpenReader("testdata/readme.zip")
	if err != nil {
		log.Fatal(err)
	}
	defer zr.Close()

	//Iter through the files in the archive,
	//printing some of their contents
	for _, f := range zr.File {
		fmt.Printf("Contents f %s:\n", f.Name)
		rc, err := f.Open()
		if err != nil {
			log.Fatal(err)
		}
		_, err = io.CopyN(os.Stdout, rc, 68)
		if err != nil {
			log.Fatal(err)
		}
		rc.Close()
		fmt.Println()
	}

	// Create a buffer to write our archive to.
	zbuf := new(bytes.Buffer)
	//create a new zip archive
	w := zip.NewWriter(zbuf)
	// add some files to the archive.
	zipFiles := []struct {
		Name, Body string
	}{
		{"readme.txt", "this archive contains some text files."},
		{"test.txt", "test file"},
		{"todo.txt", "get animal handling licence."},
	}
	for _, file := range zipFiles {
		f, err := w.Create(file.Name)
		if err != nil {
			log.Fatal(err)
		}
		_, err = f.Write([]byte(file.Body))
		if err != nil {
			log.Fatal(err)
		}
	}
	// make sure to check the error on close
	if err := w.Close(); err != nil {
		log.Fatal(err)
	}
}
