# APOJ
You provide only-**MP3** intro, samples, delimeter and outro, APOJ creates a soundtrack of "intro + reverse_sample1 + sample1 + delimiter + reverse_sample2 + sample2 + delimeter + ... + outro"

## How to run locally
### Prerequisites
- Docker

#### 1. Clone and create directories
``git clone https://github.com/donRipat/apoj.git && cd apoj && mkdir samples && mkdir intro && mkdir outro && mkdir delimiter``

#### 2. Put your samples, intro, outro and delimiter in corresponding directories

#### 3. Compose
``docker compose up``

#### 4. There should appear a result/apoj.mp3 file in your directory, enjoy :D
