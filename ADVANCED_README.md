# Advanced Readme
The at-protocol used by Bluesky has its own, sometimes convoluted, terminology. It is not necessary to know it to use the `blue-yonder` capabilities in simple applications, but you will need it to understand 'how it works' internally for creating more advanced applications. I think some imformation presented below may help you.

#### Terminology used in at-protocol and BlueSky.

- **Uniform Resource Identifier** ("**URI**") -  is a string of characters that identifies a resource on a network using at-protocol. For example, 'at://did:plc:yjvzk...246/app.bsky.feed.post/3lf...272z'.

- **Uniform Resource Locator** ("**URL**") - identifies a web resource and its location (web address). For example, 'https://bsky.app/search'.

- **Decentralized ID**s (**DID**s) - are the unique identifiers for users and other entities on BlueSky. 

- **Content ID**s (**CID**s) identify content using a digital fingerprint.

- **Record Key**s ("**rkey**s") identify individual records in a collection.

- **JASON Web Token** ("**JWT**") is used for authentication and authorization.

#### Simple and advanced usage.
You don't need to go into these details if you just want to post a post, maybe with an image or a link to an external page carefully crafted by you. Even if you want to post a long text as a sequence of plain text posts or images of pages you don't go any further. But if you want to do more and 'in your own way', you can use the advanced capabilities of the `blue-yonder` objects.

