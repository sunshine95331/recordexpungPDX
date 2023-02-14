import moment from "moment";

const today = moment().format("M/D/YYYY");

export const expectedLoginRequest = {
  data: { oeci_password: "secret", oeci_username: "username" },
  method: "post",
  url: "/api/oeci_login",
  withCredentials: true,
};

export const expectedSearchRequest = {
  data: {
    aliases: [
      {
        birth_date: "",
        first_name: "foo",
        last_name: "bar",
        middle_name: "",
      },
    ],
    demo: false,
    edits: {},
    questions: {},
    today,
  },
  method: "post",
  url: "/api/search",
  withCredentials: true,
};

export const expectedPdfRequest = {
  data: {
    aliases: [
      {
        birth_date: "",
        first_name: "foo",
        last_name: "bar",
        middle_name: "",
      },
    ],
    demo: false,
    edits: {},
    questions: {},
    today,
  },
  method: "post",
  responseType: "blob",
  url: "/api/pdf",
  withCredentials: true,
};

export const expectedPacketRequest = {
  data: {
    aliases: [
      {
        birth_date: "",
        first_name: "foo",
        last_name: "bar",
        middle_name: "",
      },
    ],
    demo: false,
    edits: {},
    questions: {},
    today,
    userInformation: {
      city: "Portland",
      date_of_birth: "12/12/1999",
      full_name: "foo bar",
      mailing_address: "1111 NE anywhere",
      phone_number: "123-456-7890",
      state: "Oregon",
      zip_code: "12345",
    },
  },
  method: "post",
  responseType: "blob",
  url: "/api/expungement-packet",
  withCredentials: true,
};

export const expectedSecondSearchRequest = {
  data: {
    aliases: [
      { birth_date: "", first_name: "foo", last_name: "bar", middle_name: "" },
      {
        birth_date: "2/23/1999",
        first_name: "fooRocky",
        last_name: "barBalboa",
        middle_name: "",
      },
    ],
    demo: false,
    edits: {},
    questions: {},
    today,
  },
  method: "post",
  url: "/api/search",
  withCredentials: true,
};

export const expectedThirdSearchRequest = {
  data: {
    aliases: [
      {
        birth_date: "2/23/1999",
        first_name: "fooRocky",
        last_name: "barBalboa",
        middle_name: "",
      },
    ],
    demo: false,
    edits: {},
    questions: {},
    today,
  },
  method: "post",
  url: "/api/search",
  withCredentials: true,
};

export const expectedCreateCaseRequest = {
  data: {
    aliases: [
      {
        birth_date: "2/23/1999",
        first_name: "fooRocky",
        last_name: "barBalboa",
        middle_name: "",
      },
    ],
    demo: false,
    edits: {
      "CASE-0001": {
        summary: {
          balance_due: "0.01",
          birth_year: "1999",
          case_number: "CASE-0001",
          current_status: "Open",
          edit_status: "ADD",
          location: "Benton",
        },
      },
    },
    questions: {},
    today: "2/13/2023",
  },
  method: "post",
  url: "/api/search",
  withCredentials: true,
};

export const expectedUpdateCaseRequest = {
  data: {
    aliases: [
      {
        birth_date: "2/23/1999",
        first_name: "fooRocky",
        last_name: "barBalboa",
        middle_name: "",
      },
    ],
    demo: false,
    edits: {
      "110000": {
        summary: {
          balance_due: "0.00",
          birth_year: "1990",
          case_number: "110000",
          current_status: "Closed",
          edit_status: "UPDATE",
          location: "Linn",
        },
      },
      "CASE-0001": {
        summary: {
          balance_due: "0.01",
          birth_year: "1999",
          case_number: "CASE-0001",
          current_status: "Open",
          edit_status: "ADD",
          location: "Benton",
        },
      },
    },
    questions: {},
    today: "2/13/2023",
  },
  method: "post",
  url: "/api/search",
  withCredentials: true,
};

export const expectedRemoveCaseRequest = {
  data: {
    aliases: [
      {
        birth_date: "2/23/1999",
        first_name: "fooRocky",
        last_name: "barBalboa",
        middle_name: "",
      },
    ],
    demo: false,
    edits: {
      "110000": { summary: { edit_status: "DELETE" } },
      "CASE-0001": {
        summary: {
          balance_due: "0.01",
          birth_year: "1999",
          case_number: "CASE-0001",
          current_status: "Open",
          edit_status: "ADD",
          location: "Benton",
        },
      },
    },
    questions: {},
    today: "2/13/2023",
  },
  method: "post",
  url: "/api/search",
  withCredentials: true,
};

export const expectedAddChargeRequest = {
  data: {
    aliases: [
      {
        birth_date: "2/23/1999",
        first_name: "fooRocky",
        last_name: "barBalboa",
        middle_name: "",
      },
    ],
    demo: false,
    edits: {
      "110000": {
        charges: {
          "110000-X03": {
            charge_type: "FareViolation",
            date: "11/12/2000",
            disposition: { date: "11/12/2000", ruling: "Dismissed" },
            edit_status: "ADD",
            level: "Felony Class A",
            name: "",
            probation_revoked: "",
          },
        },
        summary: { edit_status: "DELETE" },
      },
      "CASE-0001": {
        summary: {
          balance_due: "0.01",
          birth_year: "1999",
          case_number: "CASE-0001",
          current_status: "Open",
          edit_status: "ADD",
          location: "Benton",
        },
      },
    },
    questions: {},
    today: "2/13/2023",
  },
  method: "post",
  url: "/api/search",
  withCredentials: true,
};

export const expectedUpdateChargeRequest = {
  data: {
    aliases: [
      {
        birth_date: "2/23/1999",
        first_name: "fooRocky",
        last_name: "barBalboa",
        middle_name: "",
      },
    ],
    demo: false,
    edits: {
      "110000": {
        charges: {
          "110000-X03": {
            charge_type: "FareViolation",
            date: "11/12/2000",
            disposition: { date: "11/12/2000", ruling: "Dismissed" },
            edit_status: "ADD",
            level: "Felony Class A",
            name: "",
            probation_revoked: "",
          },
        },
        summary: { edit_status: "DELETE" },
      },
      "200000": {
        charges: {
          "200000-1": {
            charge_type: "Dismissed Criminal Charge",
            date: "4/30/1777",
            disposition: { date: "9/9/2019", ruling: "Dismissed" },
            edit_status: "UPDATE",
            level: "Misdemeanor Class A",
            name: "Obstruction of search warrant",
            probation_revoked: "",
          },
        },
        summary: { edit_status: "UPDATE" },
      },
      "CASE-0001": {
        summary: {
          balance_due: "0.01",
          birth_year: "1999",
          case_number: "CASE-0001",
          current_status: "Open",
          edit_status: "ADD",
          location: "Benton",
        },
      },
    },
    questions: {
      "210000-1": {
        ambiguous_charge_id: "210000-1",
        case_number: "210000",
        root: {
          convicted_date_string: "",
          options: {
            No: {
              edit: {},
              question: {
                convicted_date_string: "",
                options: {
                  "A Felony": { edit: { charge_type: "FelonyClassA" } },
                  "B Felony": { edit: { charge_type: "FelonyClassB" } },
                  "C Felony": { edit: { charge_type: "FelonyClassC" } },
                },
                probation_revoked_date_string: "",
                question_id:
                  "210000-1-Was the underlying substance marijuana?-No-Was the charge for an A Felony, B Felony, or C Felony?",
                selection: "",
                text: "Was the charge for an A Felony, B Felony, or C Felony?",
              },
            },
            Yes: { edit: { charge_type: "MarijuanaManufactureDelivery" } },
          },
          probation_revoked_date_string: "",
          question_id: "210000-1-Was the underlying substance marijuana?",
          selection: "",
          text: "Was the underlying substance marijuana?",
        },
      },
    },
    today: "2/13/2023",
  },
  method: "post",
  url: "/api/search",
  withCredentials: true,
};

export const expectedRemoveChargeRequest = {
  data: {
    aliases: [
      {
        birth_date: "2/23/1999",
        first_name: "fooRocky",
        last_name: "barBalboa",
        middle_name: "",
      },
    ],
    demo: false,
    edits: {
      "110000": {
        charges: {
          "110000-X03": {
            charge_type: "FareViolation",
            date: "11/12/2000",
            disposition: { date: "11/12/2000", ruling: "Dismissed" },
            edit_status: "ADD",
            level: "Felony Class A",
            name: "",
            probation_revoked: "",
          },
        },
        summary: { edit_status: "DELETE" },
      },
      "200000": {
        charges: { "200000-1": { edit_status: "DELETE" } },
        summary: { edit_status: "UPDATE" },
      },
      "CASE-0001": {
        summary: {
          balance_due: "0.01",
          birth_year: "1999",
          case_number: "CASE-0001",
          current_status: "Open",
          edit_status: "ADD",
          location: "Benton",
        },
      },
    },
    questions: {
      "210000-1": {
        ambiguous_charge_id: "210000-1",
        case_number: "210000",
        root: {
          convicted_date_string: "",
          options: {
            No: {
              edit: {},
              question: {
                convicted_date_string: "",
                options: {
                  "A Felony": { edit: { charge_type: "FelonyClassA" } },
                  "B Felony": { edit: { charge_type: "FelonyClassB" } },
                  "C Felony": { edit: { charge_type: "FelonyClassC" } },
                },
                probation_revoked_date_string: "",
                question_id:
                  "210000-1-Was the underlying substance marijuana?-No-Was the charge for an A Felony, B Felony, or C Felony?",
                selection: "",
                text: "Was the charge for an A Felony, B Felony, or C Felony?",
              },
            },
            Yes: { edit: { charge_type: "MarijuanaManufactureDelivery" } },
          },
          probation_revoked_date_string: "",
          question_id: "210000-1-Was the underlying substance marijuana?",
          selection: "",
          text: "Was the underlying substance marijuana?",
        },
      },
    },
    today: "2/13/2023",
  },
  method: "post",
  url: "/api/search",
  withCredentials: true,
};
