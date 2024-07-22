import StudyResource from "../components/StudyResource.js";

const DashBoardStud = {
  template: `<div> 
            <h1>Instructor dashboard</h1>
            <h2>New Resources</h2>
            <div v-for="res in newResources">
                <StudyResource :topic="res.topic" :content="res.content" creator="me" :approvalRequired='true' :approvalID='res.id'/>
            </div>
            <h2>Approved Resources</h2>
            <div v-for="resource in allResources">   
                    <StudyResource :topic="resource.topic" :content="resource.content" creator="me"/>
            </div>
    </div>`,
  data() {
    return {
      allResources: [],
      newResources: [],
    };
  },
  async mounted() {
    const res = await fetch(window.location.origin + "/api/resources", {
      headers: {
        "Authentication-Token": sessionStorage.getItem("token"),
      },
    });
    try {
      const data = await res.json();
      this.allResources = data;
    } catch (e) {
      console.log("error in converting to json");
    }

    // unapproved resources api call
    const resNew = await fetch(
      window.location.origin + "/api/resources/unapproved",
      {
        headers: {
          "Authentication-Token": sessionStorage.getItem("token"),
        },
      }
    );
    try {
      const data = await resNew.json();
      this.newResources = data;
    } catch (e) {
      console.log("error in converting to json");
    }
  },
  components: { StudyResource },
};

export default DashBoardStud;
