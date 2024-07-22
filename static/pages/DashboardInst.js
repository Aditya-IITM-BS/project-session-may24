import StudyResource from "../components/StudyResource.js";

const DashBoardStud = {
  template: `<div>
            <h1>Instructor dashboard</h1>
            <h2>New Resources</h2>
            <div v-for="res in newResources">
            <StudyResource :topic="res.topic" :content="res.content" creator="me" :approvalRequired=true :approvalID="res.id" />
            </div>

            <h2>Approved Resources </h2>
            <div v-for="resource in allResources">   
                    <StudyResource :topic="resource.topic" :content="resource.content" creator="me"/>
            </div>
    </div>`,
  data() {
    return {
      newResources: [],
      allResources: [],
    };
  },
  async mounted() {
    const resNewRes = await fetch(
      window.location.origin + "/api/resources/unapproved",
      {
        headers: {
          "Authentication-Token": sessionStorage.getItem("token"),
        },
      }
    );
    if (resNewRes.ok) {
      this.newResources = await resNewRes.json();
    }

    const resAllRes = await fetch(window.location.origin + "/api/resources", {
      headers: {
        "Authentication-Token": sessionStorage.getItem("token"),
      },
    });

    if (resAllRes.ok) {
      const data = await resAllRes.json();
      this.allResources = data;
    }
  },
  components: { StudyResource },
};

export default DashBoardStud;
