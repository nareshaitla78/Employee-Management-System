<template  >


        <div :class="'q-pa-md'">
          <div :class="'flex justify-end m-2'">
            <q-btn label="ADD NEW Employee"    @click="showemployeeDetails=!showemployeeDetails" :class="'text-white bg-gradient-to-r from-purple-500 to-pink-500 hover:bg-gradient-to-l focus:ring-4 focus:outline-none focus:ring-purple-200 dark:focus:ring-purple-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 justify-self-end'"/>
            <q-btn @click="backToOfficeDetails"  label="Back"  :class="'text-white bg-gradient-to-r from-purple-500 to-pink-500 hover:bg-gradient-to-l focus:ring-4 focus:outline-none focus:ring-purple-200 dark:focus:ring-purple-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2'" />
          </div>
          <div>
              <q-dialog v-model="showemployeeDetails">
              <div class="q-pa-md"  :class="'w-full bg-white'" style="max-width: 700px;" >

                <q-form
                  @submit.prevent="onSubmit('top')"

                  class="q-gutter-md"
                >
                  <q-input
                    filled
                    v-model="employeeNumber"
                    label="employeeNumber*"
                    :class="'text-blue-50'"
                    hint="Enter employeeNumber"
                    lazy-rules
                    :rules="[ val => validateInteger(val) && val> 0 || 'Please Enter Employee Number and must be Integer' ]"
                  />
                  <q-input
                    filled
                    v-model="lastName"
                    label="lastName*"
                    hint="Enter lastName"
                    lazy-rules
                    :rules="[ val => val && val.length > 0 || 'Please type LastName']"
                  />
                  <q-input
                    filled
                    v-model="firstName"
                    label="firstName*"
                    hint="Enter firstName"
                    lazy-rules
                    :rules="[ val => val && val.length > 0 || 'Please type firstName']"
                  />
                  <q-input
                    filled
                    v-model="extension"
                    label="extension*"
                    hint="Enter extension"
                    lazy-rules
                    :rules="[ val => val && val.length > 0 || 'Please type extension']"
                  />
                  <q-input
                    filled
                    v-model="email"
                    label="email*"
                    hint="Enter email"
                    lazy-rules
                    :rules="[(val) => validateEmail(val) || 'Must be in this format @classicmodelcars.com']"
                  />
                  <q-input
                    filled
                    v-model="officeCode"
                    label="officeCode*"
                    hint="Enter officeCode"
                    lazy-rules
                    :rules="[ val=>validateInteger(val)|| '  officeCode should be Integer']"
                  />
                  <q-input
                    filled
                    v-model="reportsTo"
                    label="reportsTo*"
                    hint="Enter reportsTo"
                    lazy-rules
                    :rules="[ val => validateInteger(val) || 'reportsTo  should be Integer which are already in Db']"
                  />
                  <q-input
                    filled
                    v-model="jobTitle"
                    label="jobTitle*"
                    hint="Enter jobTitle"
                    lazy-rules
                    :rules="[ val => val && val.length > 0 || 'Please type jobTitle']"
                  />



                  <div>
                    <q-btn   label="Save" type="submit" color="primary" />
                    <q-btn flat label="Cancel" color="primary" v-close-popup />
                  </div>
                  <!-- <q-notify v-if="formSubmitted" icon=""   class="text-green flex justify-center" >*Employee Details Submitted Successfully</q-notify> -->

                </q-form>

            </div>
            </q-dialog>
          </div>

          <div :class="'w-full max-h-full'">
            <q-table color="green-8" title="Employees Details" separator="cell" :card-class="'bg-white'"  :columns="columns" :rows="rows" class="card">
            </q-table>
          </div>
        </div>
</template>

<script>
import { data } from "autoprefixer";
import {useQuasar} from "quasar"
import {ref} from "vue"
const columns = [
  { name: "employeeNumber", label: "EmployeeNumber", field: "employeeNumber",align:"center"  },
  { name: "lastName", label: "LastName", field: "lastName",align:"center" },
  { name: "firstName", label: "FirstName", field: "firstName",align:"center" },
  { name: "extension", label: "Extension", field: "extension" ,align:"center"},
  { name: "email", label: "Email", field: "email" ,align:'center'},
  { name: "officeCode", label: "OfficeCode", field: "officeCode" ,align:"center"},
  { name: "reportsTo", label: "ReportsTo", field: "reportsTo",align:"center" },
  { name: "jobTitle", label: "JobTitle", field: "jobTitle" ,align:"center"},

];
  export default {
    data(){
      const $q=useQuasar()
      return {
        columns,rows:[],
        formSubmitted:false,
        showemployeeDetails:false,
          employeeNumber :'',
          lastName :'',
          firstName:'',
          extension:'',
          email:'',
          officeCode:'',
          reportsTo:'',
          jobTitle:''
      }
    },
    methods:{
      fetchclickedData(){
        let self=this
        this.$axios.get(`/api/get_office_employees/${self.$route.params.officeCode}/`)
        .then(function(response){
          self.rows=response.data.data
        })
      },
      onSubmit(){
        // if(this.employeeNumber<=0 || this.lastName.length<=2 || this.firstName.length<=2 ||
        // this.extension.length<=3 || this.email==this.email.endsWith("@classicmodelcars.com") || this.officeCode<=0 || this.reportsTo.length<=2 || this.jobTitle.length){
        //   return "error"

        // }
        let self = this


        self.formSubmitted=true;
        let formData={
          employeeNumber:self.employeeNumber,
          lastName:self.lastName,
          firstName:self.firstName,
          extension:self.extension,
          email:self.email,
          officeCode:self.officeCode,
          reportsTo:self.reportsTo,
          jobTitle:self.jobTitle

        }


      self.$axios.post(`/api/new_employee/${self.officeCode}/`,formData)
      .then(function(response){
         let data=response
         if(response.data.ok){
          console.log("hello 1")
          self.showemployeeDetails=false;
          self.$q.notify({
            message:"submitted succeesfully",
            color:'green',
            position:'top'
          })
         } else {
          console.log(response.data)
          self.$q.notify({
            message: response.data.error,
            color:'red',
            position:'top'
          })
         }

      })
      .catch((error)=>{
        console.log(error)
        this.$q.notify({
          message: "an error occured wh" ,
          color:'red',
          position:'top'
        })
      })

      },
      validateEmail(email){
       // @classicmodelcars
      return /[a-z0-9]+\.[a-z]{2,3}/.test(email);
      },
      validateInteger(toreport){
            return /[0-9]/.test(toreport)
      }
      ,
      backToOfficeDetails(){
        this.$router.push("/")
      },



    },
    created(){
      this.fetchclickedData()
    }
  }
</script>

<style lang="scss" scoped>




</style>
