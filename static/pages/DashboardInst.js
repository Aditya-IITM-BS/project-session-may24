import StudyResource from "../components/StudyResource.js";

const DashboardInst = {
  template: `<div><h1>This is Instructor dashboard {{test}}</h1>
              <div d-flex flex-row p-5 v-for="resource in allResources">
                <StudyResource :topic="resource.topic" :content="resource.content" :creator="resource.creator" :approvalRequired="true" />
              </div>
          </div>`,
  components: {
    StudyResource,
  },
  data() {
    return {
      test: this.$store.state.test,
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

export default DashboardInst;
