# SongAI
- A fullstack application that turns singing or typed lyrics into a music video.

## Running the application
- Globally install all the required python libraries with pip
    - moviepy
    - nltk
    - unicode
    - contractions

- In base directory run `npm install` and then `npm start`.
- Application will run on localhost port 3000.

HackUMass X Project Submission Guidelines

- HackUMass X projects should be submitted on Devpost at hackumass-x.devpost.com. The HackUMass X Dashboard will not be used for project submissions, so do not worry if you are not able to see a project submission portal there.
For the project description on Devpost, we are interested in the following details:
Inspiration: We want to know more about what inspired you to build this project, why it matters to you, and how your project builds on this. For example, does your project contribute to computing for the common good? Were you inspired by a problem you have faced personally?

    - We were inspired to create a fun interdisciplinary software project that used our collective experience in linguistics, NLP/artificial intelligence, scripting and front end UI/UX. The seed initially started with two of our members, one studying linguistics and compsci, and the other studying data science and compsci. As our team grew, members with experience in HTML, CSS, and NodeJS were inspired to build a fun web-based UI to give the project some life. Creative members with scripting talent added even more fun ideas by rendering custom video files.

- What it does: Elucidate what your project exactly does, briefly describing its functionalities and features. Be sure to list how each feature adds value to the overall project or its focal idea.

    - Our project used natural language processing (Naive Bayes) trained on a song lyric dataset to classify the genre of the song. It takes text input, but creative members of our team added speech to text functionality to allow users to sing the song instead. We then use that genre to generate a custom music video, using moviepy, and overlay that with either a text to speech library, or the raw audio from the user if they choose to sing. We also add a background beat from freely available music from the classified genre.

- How we built it: Present how you approached your idea, and what HackUMass resources you used to improve your project, if any. Did any workshops help you pick up new skills? Did you receive support from mentors or organizers? Were you and your teammates collaborating virtually?

    - We had members who all had a good idea about how to implement some facet of this project already, the tricky part was figuring out how we could tie it all together cohesively. Members who have focused their studies on backend work such as AI/ML and NLP had little front end knowledge, and conversely users with extensive front end knowledge had little to no experience training a model. We all had to pick up new skills such as git to be able to work together well, and most of us worked with tools or libraries that we never have before, such as moviepy and various NodeJS modules.

- Challenges we ran into: Speak about the blocks and challenges you faced while ideating for or building your project, and how you overcame them. Was there any impediment to your teamwork? Were you not able to figure out how to use your hardware effectively? Was there a faulty library that crashed your app?

    - The most significant challenge was designing the model. Specifically, trying to train multi-label linear regression on a considerable set of possible labels (almost 80). This ended up failing quite miserably, as some labels were too sparse, and the model had a very hard time converging to fit the training set. Ideally, this would be solved using K nearest neighbors, and while our ML experts had a good conceptual understanding of why that would be effective, they had no experience in training such a mode. Ultimately, it was decided that we would have to throw out some data and reduce our genres to 1 of 11 possible labels. We also decided that naive bayes was going to be necessary, as we were adamant about not using an off the shelf library, and it will always produce a result. There were also various headaches with git, as well as conflicting nodejs modules that we lost significant time debugging. 

- Accomplishments you are proud of: Tell us about the exciting achievements and triumphs you had in the process of building your project! Did you run a server on the first attempt? Did your team have excellent communication? Was your project completed in less than 24 hours?
We had a shaky start with loosing several group members, but we quickly found other members and manage to pull together a real MVP for a fairly ambitious project. We don’t think this project will do much good for the world, aside from providing a few laughs, but we did demonstrate our ability to construct an interdisciplinary project. Not only that, but we were proud of designing a model that, while far from ideal in terms of raw accuracy, makes quite reasonable classifications for most songs during our testing. We were super excited to be able to pull together work done mostly independently by our members into a reasonably polished MVP. The front end, while not the most visually exiting, is clean and functional, and will translate well to a remotely hosted web app in the near feature.
What you learned: Describe what your takeaways were from this experience, mentioning some of the skills you gained or tooling you became familiar with. Are you now comfortable with web programming? Did you get acquainted with Arduinos? Have you enjoyed working with AWS provisions?

    - The biggest takeaway that we had was actually learning to work on a project as a team that none of us could have done by ourselves. We all worked collaboratively, but mostly independently in terms of implementation, to bring our idea to life. We learned about how to be flexible with what we are implementing, and how to pivot when parts of our project needed to change. Likewise, we learned how to budget time by setting deadlines for when our deliverables would be ready. We also learned about the reality of how missing those deadlines can through a project off, and how to abstract our work, so we didn’t actually need those deliverables until the very end. This required good communication about the various APIs we were all creating because doing so enabled the black box abstraction that we needed to complete a project with many moving parts in a short period of time.

- What's next for your hack: Where do you see your hack going? Talk about what your plans are for this hack, and what’s your vision with the goal you had set out with, if any. Will you build upon this hack separately? Will you use it as a learning opportunity, and start fresh on a new hackathon?

    - We were really hoping to get the whole project contained in a remotely hosted web app, either on AWS or Azure. We also wanted to do some work with audio compression, specifically uncompressed WAV to V0 MP3 using LAME, and compressing the x264 MP4 video files to lower bit rate x265 encodes using handbrake to speed up processing time. Furthermore, we would really like to use some kind of AI-generated images using something like DALL*E from open AI to have an even more customized experience.

Do not forget to select up to 3 prize categories that your project will be considered for!


