# cicd-gaia-python-example
Gaia CICD Python Example


## Usage

Setup Gaia on Docker:

```
> docker run -d -p 8080:8080 -v $PWD:/data gaiapipeline/gaia:latest
```

Go to [http://localhost:8080/](http://localhost:8080):

<img width="1083" alt="image" src="https://user-images.githubusercontent.com/30043398/74637810-64a75c00-5173-11ea-90fb-445b53ffa851.png">

Credentials: admin/admin

<img width="1085" alt="image" src="https://user-images.githubusercontent.com/30043398/74637881-8b659280-5173-11ea-8740-cf93fe17249b.png">

Create a Pipeline:

<img width="1422" alt="image" src="https://user-images.githubusercontent.com/30043398/74637991-c5cf2f80-5173-11ea-8ab2-dd8916e70f98.png">

You can fork: [https://github.com/ruanbekker/cicd-gaia-python-example](https://github.com/ruanbekker/cicd-gaia-python-example)

<img width="1424" alt="image" src="https://user-images.githubusercontent.com/30043398/74638119-fe6f0900-5173-11ea-9f54-761b01afe366.png">

Create the Pipeline, then you should see it under your pipelines after a minute or so:

<img width="1422" alt="image" src="https://user-images.githubusercontent.com/30043398/74638243-38d8a600-5174-11ea-8255-54cdfedf7051.png">

Start the Pipeline:

<img width="1422" alt="image" src="https://user-images.githubusercontent.com/30043398/74638324-60c80980-5174-11ea-8fa0-1fc0504074e8.png">

We can then view the logs:

<img width="1425" alt="image" src="https://user-images.githubusercontent.com/30043398/74638386-76d5ca00-5174-11ea-91bd-03bb8470192e.png">

When we go back to the overview, we will see that our pipeline succeeded:

<img width="1424" alt="image" src="https://user-images.githubusercontent.com/30043398/74638432-8bb25d80-5174-11ea-92f2-c5629bc18f75.png">
