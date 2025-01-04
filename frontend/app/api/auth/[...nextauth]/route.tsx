import NextAuth from 'next-auth/next';
import GoogleProvider from 'next-auth/providers/google'


export const authOptions ={
    providers: [
        GoogleProvider({
          clientId: process.env.GOOGLE_ID ?? (() => { throw new Error('GOOGLE_ID is not defined'); })(),
          clientSecret: process.env.GOOGLE_SECRET ?? (() => { throw new Error('GOOGLE_SECRET is not defined'); })(),
        }),
      ],
    //   callbacks:{
    //     session:({session,token,user})=>{
    //       if (adminEmails.includes(session?.user?.email))
    //       {
    //         return session;
    //       }
    //       else{
    //         return false;
    //       }
    //     }
    //   },
};

export const handler = NextAuth(authOptions)
export {handler as GET , handler as POST};