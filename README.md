# containertools/hello-world
Sample container image for testing.

## Usage
To create the image containertools/hello-world, execute the following command:
```shell
docker build -t containertools/hello-world .
```

Running your Hello World container:
```shell
docker run -it -p 8080:8080 containertools/hello-world
```

Running your Hello World container mouting a files directory:
```shell
docker run -it -p 8080:8080 -v "$PWD/files:/files" -e FILES_BASEPATH=/files containertools/hello-world
```

## Environment Variables
`FILES_BASEPATH`: Path to the directory containing the files to be listed. Default value: `/tmp`

## Endpoints
- [/](http://localhost:8080/): Shows an HTML page containing some container configuration information.
- [/json](http://localhost:8080/json): Shows a JSON object containing some container configuration information.
- [/files](http://localhost:8080/files): List files in the `FILES_BASEPATH` directory.