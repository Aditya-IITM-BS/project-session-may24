import StudyResource from "../components/StudyResource.js";

const DashboardStud = {
  template: `<div><h1>This is student dashboard</h1>
              <div d-flex flex-row p-5 v-for="resource in allResources">
                <StudyResource :topic="resource.topic" :content="resource.content" :creator="resource.creator" />
              </div>
          </div>`,
  components: {
    StudyResource,
  },
  data() {
    return {
      allResources: [
        {
          topic: "topic 1",
          content:
            "some random contend lorem ipsum this is very long content and this can be used to test if ellipses is working properly",
          creator: "student1",
        },
        {
          topic: "topic 2",
          content:
            "some random contend lorem ipsum this is very long content and this can be used to test if ellipses is working properly",
          creator: "student1",
        },
        {
          topic: "topic 3",
          content:
            "some random contend lorem ipsum this is very long content and this can be used to test if ellipses is working properly",
          creator: "student1",
        },
      ],
    };
  },
};

export default DashboardStud;
