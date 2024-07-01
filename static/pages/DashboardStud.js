import StudyResource from "../components/StudyResource.js";

const DashBoardStud = {
  template: `<div> 
            <h1>this is student dashboard</h1>
            <div v-for="resource in allResource">   
                    <StudyResource :topic="resource.topic" :content="resource.content" creator="me"/>
            </div>
    </div>`,
  data() {
    return {
      allResource: [],
    };
  },
  async mounted() {
    const res = await fetch(window.location.origin + "/api/resources");
    const data = await res.json();
    this.allResource = data;
  },
  components: { StudyResource },
};

export default DashBoardStud;
