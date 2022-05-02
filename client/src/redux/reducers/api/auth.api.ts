import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { ROUTES } from "../../constants";
import { addAuthHeader } from "./helpers";
import { AuthPage, AuthPayload, EmittedToken, RegisterPayload } from "../types";
import {
  changeAuthPage,
  changeEmail,
  changePasswordInput,
  changeSecondPasswordInput,
} from "../auth";

export const authApi = createApi({
  reducerPath: "authApi",
  baseQuery: fetchBaseQuery({
    baseUrl: ROUTES.AUTH.BASE,
    prepareHeaders: addAuthHeader,
  }),
  endpoints: (builder) => ({
    auth: builder.mutation<EmittedToken, AuthPayload>({
      query: (body) => ({
        url: ROUTES.AUTH.LOGIN,
        method: "POST",
        body,
      }),
      async onQueryStarted(_, { queryFulfilled }) {
        try {
          const token = await queryFulfilled;
          localStorage.authToken = token.data.access_token;
        } catch {
          localStorage.authToken = "";
        }
      },
    }),
    // TODO: unsafe register, rework after back ready
    register: builder.mutation<EmittedToken, RegisterPayload>({
      query: (body) => ({
        url: ROUTES.AUTH.REGISTER,
        method: "POST",
        body: {
          ...body,
          is_active: true,
          is_superuser: false,
          is_verified: false,
        },
      }),
      async onQueryStarted(_, { dispatch, queryFulfilled }) {
        try {
          const { meta } = await queryFulfilled;
          if (meta?.response?.ok) {
            dispatch(changeEmail(""));
            dispatch(changePasswordInput(""));
            dispatch(changeSecondPasswordInput(""));
            dispatch(changeAuthPage(AuthPage.auth));
          }
        } catch {}
      },
    }),
  }),
});

export const { useAuthMutation, useRegisterMutation } = authApi;
export default authApi.reducer;
