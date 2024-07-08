const AddResource = {
  template: `<div>
    <h2>Add Resource</h2>
    <form @submit.prevent="submitForm">
      <label for="topic">Topic:</label>
      <input type="text" id="topic" v-model="topic" required><br><br>

      <label for="content">Content:</label>
      <textarea id="content" v-model="content" required></textarea><br><br>

      <label for="creatorId">Creator ID:</label>
      <input type="text" id="creatorId" v-model="creatorId" required><br><br>

      <button type="submit">Add Resource</button>
    </form>
  </div>`,
  data() {
    return {
      topic: "",
      content: "",
      creatorId: "",
    };
  },
  methods: {
    submitForm() {
      const backendUrl = window.location.origin + "/api/resources"; // Replace with your backend URL

      // Prepare data for POST request
      const postData = {
        topic: this.topic,
        content: this.content,
        creator_id: this.creatorId,
      };

      // Fetch API POST request
      fetch(backendUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authentication-Token": localStorage.getItem("token"),
        },
        body: JSON.stringify(postData),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          console.log("Resource added:", data);
          // Optionally show success message or redirect
        })
        .catch((error) => {
          console.error("Error adding resource:", error);
          // Handle error, show error message, etc.
        });
    },
  },
};
