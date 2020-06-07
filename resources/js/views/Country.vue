<template>
  <div class="row">
    <div class="col text-center">
      <h2>Lista de poblacion por continente</h2>
      <div class="col-md-12">
        <div class="col-md-6">
          <div class="row">
            <form @submit.prevent="importdb()" method="post">
            <button
              type="submit"
              :disabled="pages.length > 0"
              class="btn btn-primary"
            >
              Importar a DB
            </button>
            </form>
            <div class="m-1"></div>
            <form @submit.prevent="cleardata()" method="post">
              <button
                :disabled="pages.length == 0"
                type="submit"
                class="btn btn-danger"
              >
                Limpiar Datos
              </button>
            </form>
          </div>
        </div>
        <div class="mb-1"></div>
        <table class="table table-hover table-striped">
          <thead>
            <th>#</th>
            <th>Continente</th>
            <th>Codigo Iso</th>
            <th>Año</th>
            <th>Poblacion Total</th>
          </thead>
          <tbody v-if="pages.length > 0">
            <tr v-for="(country, index) in pages" :key="country.id">
              <td>{{ index + 1 }}</td>
              <td>{{ country.name }}</td>
              <td>{{ country.countryisocode }}</td>
              <td>{{ country.date }}</td>
              <td>{{ new Intl.NumberFormat().format(country.quantity) }}</td>
              
            </tr>
            <tr>
              
            </tr>
          </tbody>
          <div v-else>
            <p>No results</p>
          </div>
        </table>
        <paginate :items="countries" @changePage="onChangePage"> </paginate>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Swal from "sweetalert2";
import "sweetalert2/dist/sweetalert2.min.css";
export default {
  
  data() {
    return {
      country: {
        name: "",
        countryisocode: "",
        date: "",
        quantity: "",
      },
      page: "",
      countries: [],
      dataexp: [],
      pages: [],
    };
  },
 
  created() {
    this.getDatadb();
  },
  methods: {
    onChangePage(pageOfItems) {
      // update page of items
      this.pages = pageOfItems;
    },

    importdb() {
      Swal.fire({
        title: "¿Estas seguro?",
        text: "Con este boton importará los datos de la Api a la Base de datos",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, importar los datos!",
      }).then((result) => {
        if (result.value) {
          return new Promise((resolve, reject) => {
            let urlapi = `https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?date=2017:2018&format=json`;
            axios
              .get(urlapi)
              .then((response) => {
                this.$data.dataexp = response.data[1];
                let dataexp = JSON.parse(JSON.stringify(this.$data.dataexp));

                dataexp.map(function(data) {
                  let country = {
                    name: data.country.value,
                    countryisocode: data.countryiso3code,
                    date: data.date,
                    quantity: data.value,
                  };

                  const path = `http://localhost:8000/api/v1.0/countries/`;
                  axios.post(path, country, { headers: { "x-csrftoken": $cookies.get("csrftoken") } })
                    .then((response) => {
                      //console.log(response);
                    })
                    .then(
                      Swal.fire(
                        "Importacion correcta!",
                        "Los datos han sido importados satisfactoriamente.",
                        "success"
                      )
                    )
                    .catch((error) => {
                      console.log(error);
                    });
                });
                this.getDatadb();
                resolve();
              })
              .catch((error) => {
                console.log(error);
                reject();
              });
          });
        }
      });
    },

    getCountries() {
      let url = `http://localhost:8000/v2/country/all/indicator/SP.POP.TOTL?date=2017:2018&format=json`;
      axios
        .get(url)
        .then((response) => {
          this.$data.dataexp = response.data[1];
          return this.$data.dataexp;
          // this.pages = response.data[1]
          // this.countries = response.data[1];
        })
        .catch((error) => {
          console.log(error);
        });
    },

    cleardata() {
      let cookie = $cookies.get("csrftoken");
      Swal.fire({
        title: "¿Estas seguro?",
        text: "Con este boton eliminara la informacion de la base de datos",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, eliminarlos!",
      }).then((result) => {
        if (result.value) {
          return new Promise((resolve, reject) => {
            const path = `http://localhost:8000/delcountries`;
            axios
              .post(path, {}, { headers: { "x-csrftoken": $cookies.get("csrftoken") } })
              .then((response) => {
                //console.log(response)
                Swal.fire("Eliminados!", "La informacion ha sido eliminada satisfactoriamente.", "success");
                this.getDatadb();
                resolve();
              })
              .catch((error) => {
                console.log(error);
              });
          });
        }
      });
    },
    getDatadb() {
      const path = `http://localhost:8000/api/v1.0/countries/`;
      axios
        .get(path)
        .then((response) => {
          //console.log(response.data)
          this.pages = response.data;
          this.countries = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  computed:{
    getCurrentIndex: function(index){
       
    }
  }
};
</script>
