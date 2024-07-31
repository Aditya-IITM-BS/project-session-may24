import StudyResource from "../components/StudyResource.js";

const DashBoardStud = {
  template: `<div> 
            <h1>this is student dashboard</h1>
            <button @click='downloadCSV'>download</button>
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
    const res = await fetch(window.location.origin + "/api/resources", {
      headers: {
        "Authentication-Token": sessionStorage.getItem("token"),
      },
    });
    console.log(res.ok);

    if (res.ok) {
      const data = await res.json();
      this.allResource = data;
    }
  },
  methods : {
    async downloadCSV(){
      const res = await fetch(window.location.origin + "/start-export")
      const data = await res.json()
  
      const taskID = data['task_id']
  
      const intervalPoll = setInterval(async () => {
        const taskRes = await fetch(window.location.origin + "/download-export/" + taskID)
  
        if (taskRes.ok){
          console.log('task completed')
          window.open(window.location.origin + "/download-export/" + taskID)
          clearInterval(intervalPoll)
        }
        }, 1000)
      },
  },
  
  components: { StudyResource },
};

export default DashBoardStud;
