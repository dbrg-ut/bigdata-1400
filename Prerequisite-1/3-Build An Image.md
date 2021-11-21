## Running A Sample App From Scratch



#### You can Follow These Instructions Locally :
```bash
$ docker run -dp 800:80 docker/getting-started
$ # Visit : http://localhost:800
```



#### Build a Sample To-Do App in Node JS

- extract app.zip

- Create a file named `Dockerfile` in the same folder as the file `package.json` with the following contents.

  ```
  FROM node:12-alpine
  WORKDIR /app
  COPY . .
  RUN yarn install --production
  CMD ["node", "src/index.js"]
  ```

- If you haven't already done so, open a terminal and go to the `app` directory with the `Dockerfile`. Now build the container image using the `docker build` command.

  ```
  docker build -t getting-started .
  ```

- Check Image has been created : 

  ```bash
  $ docker images
  ```

- Run The App : 
  ```bash
  docker run -dp 3000:3000 getting-started
  ```

​    

- In the `src/static/js/app.js` file, update line 56 to use the new empty text.

  ```html
  <p className="text-center">You have no todo items yet! Add one above!</p>
  
  ```
  
- Build Again :
 ```
  docker build -t getting-started .
 ```
-  Run :
   ```bash
    $ docker run -dp 3000:3000 getting-started
   ```
    You See An Error! - Port 3000 is already in use. rm the running app 
   
