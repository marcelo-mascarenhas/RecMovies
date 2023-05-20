
import { getMovieInfo } from "../getMovie";
import api from "../../api";
import axios from "axios";

describe("services", () => {
    describe("api", () => {
      let result;
      beforeAll(async () => {
        jest.clearAllMocks();
        axios.get.mockResolvedValue({
                "Avatar":{
                    title: "Avatar",
                    language: "en"
                },
                "Avatar 3":{
                    title: "Avatar 3",
                    language: "en"
                },
        })
        result = await getMovieInfo("Avatar");
      });
  
      it("should return the mock data", () => {
        expect(result).toEqual({
            "Avatar":{
                title: "Avatar",
                language: "en"
            },
            "Avatar 3":{
                title: "Avatar 3",
                language: "en"
            },
        });
      });
  
    });
  });


