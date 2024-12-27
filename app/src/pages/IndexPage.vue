<template>
  <q-page class="flex justify-center top">
     <div :class="'text-white w-full m-5'" >
      <q-table
      flat
      bordered
      :card-class="'bg-white'"
      title="Office Details"
      separator="cell"
      :rows="rows"
      :columns="columns"
      row-key="officeCode"
      class="my-sticky-header-column-table"
    >
      <template v-slot:body-cell-officeCode="props" >
        <q-td :props="props">
          <div @click="onOfficeCodeClick(props.value)" :class="'cursor-pointer rounded-sm'">
            <q-badge square color="amber">{{ props.value }}</q-badge>
          </div>
        </q-td>
      </template>
    </q-table>
     </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import { useOfficeStore } from "src/stores/OfficeStore";
import { colors } from "quasar";

const officeStore = useOfficeStore();

const columns = [
  { name: "officeCode", label: "OfficeCode", field: "officeCode" ,align:"center" ,color:"red"},
  { name: "city", label: "City", field: "city",align:"center" },
  { name: "phone", label: "Phone", field: "phone" ,align:"center"},
  { name: "addressLine1", label: "AddressLine1", field: "addressLine1" ,align:"center"},
  { name: "addressLine2", label: "AddressLine2", field: "addressLine2" ,align:"center"},
  { name: "state", label: "State", field: "state",align:"center" },
  { name: "country", label: "Country", field: "country" ,align:"center"},
  { name: "postalCode", label: "PostalCode", field: "postalCode",align:"center" },
  { name: "territory", label: "Territory", field: "territory",align:"center" },
];
export default defineComponent({
  name: "IndexPage",
  data() {
    return {
      officeStore: officeStore,
      columns,
      rows: [],

    };
  },

  methods: {
    fetchOfficeData() {
      let self = this;
      this.$axios
      .get("/api/office/")
      .then(function (response) {
        console.log("response.data...", response.data.data);
        self.rows = response.data.data;
      });
    },

    onOfficeCodeClick(officeCode) {
      console.log("officeCode", officeCode);
      this.$router.push(`/offices/${officeCode}/employees/`);
    },
  },

  created() {
    this.fetchOfficeData();
  },

  mounted() {},
});
</script>
