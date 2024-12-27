import { defineStore } from "pinia";
import officeData from "../../../offices.json"
import axios from "src/boot/axios";

export const useOfficeStore = defineStore("offices",{
  state:()=>({
    offices: officeData
  }),
  actions:{

  }
})
