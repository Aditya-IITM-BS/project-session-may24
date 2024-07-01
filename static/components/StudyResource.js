const StudyResource = {
  template: `<div>
    <div class="card shadow-sm p-4 mb-4 study-resource-card" @click="openPopup">
      <div class="card-body">
        <h3 class="card-title text-center mb-3 text-primary text-truncate">{{ topic }}</h3>
        <p class="card-text text-secondary text-truncate">{{ content }}</p>
      </div>
      <div class="card-footer text-muted text-end">
        <small>Created by: {{ creator }}</small>
      </div>
    </div>
    <div v-if="showPopup" class=" popup-overlay d-flex align-items-center justify-content-center">
    <div class="popup-content card shadow p-4">
      <h3 class="card-title text-center mb-3 text-primary">{{ topic }}</h3>
      <p class="card-text text-secondary">{{ content }}</p>
      <div class="text-muted text-end mt-3">
        <small>Created by: {{ creator }}</small>
      </div>
      <button v-show="approvalRequired" class="btn btn-success mt-3" @click="sendApproval">Approve</button>
      <button class="btn btn-secondary  mt-3" @click="closePopup">Close</button>
    </div>
  </div>
  </div>`,
  props: {
    topic: {
      type: String,
      required: true,
    },
    content: {
      type: String,
      required: true,
    },
    creator: {
      type: String,
    },
    approvalRequired: {
      type: Boolean,
    },
    approvalID: {
      type: String,
    },
  },
  data() {
    return {
      showPopup: false,
    };
  },
  methods: {
    openPopup() {
      this.showPopup = true;
    },
    closePopup() {
      this.showPopup = false;
    },
  },
  mounted() {
    const style = document.createElement("style");
    style.textContent = `
      .study-resource-card {
        max-width: 600px;
        margin: auto;
        border-radius: 15px;
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
      }
      .study-resource-card:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
      }
    `;
    document.head.appendChild(style);
  },
};

export default StudyResource;
