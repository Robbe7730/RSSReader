/* tslint:disable */
/* eslint-disable */
/**
 * PostgREST API
 * This is a dynamic API generated by PostgREST
 *
 * The version of the OpenAPI document: 7.0.1 (UNKNOWN)
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import * as runtime from '../runtime';
import {
    Feeds,
    FeedsFromJSON,
    FeedsToJSON,
} from '../models';

export interface FeedsDeleteRequest {
    id?: number;
    name?: string;
    url?: string;
    priority?: number;
    hidden?: boolean;
    createdAt?: string;
    updatedAt?: string;
    prefer?: FeedsDeletePreferEnum;
}

export interface FeedsGetRequest {
    id?: number;
    name?: string;
    url?: string;
    priority?: number;
    hidden?: boolean;
    createdAt?: string;
    updatedAt?: string;
    select?: string;
    order?: string;
    range?: string;
    rangeUnit?: string;
    offset?: string;
    limit?: string;
    prefer?: FeedsGetPreferEnum;
}

export interface FeedsPatchRequest {
    id?: number;
    name?: string;
    url?: string;
    priority?: number;
    hidden?: boolean;
    createdAt?: string;
    updatedAt?: string;
    prefer?: FeedsPatchPreferEnum;
    feeds?: Feeds;
}

export interface FeedsPostRequest {
    select?: string;
    prefer?: FeedsPostPreferEnum;
    feeds?: Feeds;
}

/**
 * 
 */
export class FeedsApi extends runtime.BaseAPI {

    /**
     */
    async feedsDeleteRaw(requestParameters: FeedsDeleteRequest): Promise<runtime.ApiResponse<void>> {
        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.id !== undefined) {
            queryParameters['id'] = requestParameters.id;
        }

        if (requestParameters.name !== undefined) {
            queryParameters['name'] = requestParameters.name;
        }

        if (requestParameters.url !== undefined) {
            queryParameters['url'] = requestParameters.url;
        }

        if (requestParameters.priority !== undefined) {
            queryParameters['priority'] = requestParameters.priority;
        }

        if (requestParameters.hidden !== undefined) {
            queryParameters['hidden'] = requestParameters.hidden;
        }

        if (requestParameters.createdAt !== undefined) {
            queryParameters['created_at'] = requestParameters.createdAt;
        }

        if (requestParameters.updatedAt !== undefined) {
            queryParameters['updated_at'] = requestParameters.updatedAt;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        if (requestParameters.prefer !== undefined && requestParameters.prefer !== null) {
            headerParameters['Prefer'] = String(requestParameters.prefer);
        }

        const response = await this.request({
            path: `/feeds`,
            method: 'DELETE',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.VoidApiResponse(response);
    }

    /**
     */
    async feedsDelete(requestParameters: FeedsDeleteRequest): Promise<void> {
        await this.feedsDeleteRaw(requestParameters);
    }

    /**
     */
    async feedsGetRaw(requestParameters: FeedsGetRequest): Promise<runtime.ApiResponse<Array<Feeds>>> {
        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.id !== undefined) {
            queryParameters['id'] = requestParameters.id;
        }

        if (requestParameters.name !== undefined) {
            queryParameters['name'] = requestParameters.name;
        }

        if (requestParameters.url !== undefined) {
            queryParameters['url'] = requestParameters.url;
        }

        if (requestParameters.priority !== undefined) {
            queryParameters['priority'] = requestParameters.priority;
        }

        if (requestParameters.hidden !== undefined) {
            queryParameters['hidden'] = requestParameters.hidden;
        }

        if (requestParameters.createdAt !== undefined) {
            queryParameters['created_at'] = requestParameters.createdAt;
        }

        if (requestParameters.updatedAt !== undefined) {
            queryParameters['updated_at'] = requestParameters.updatedAt;
        }

        if (requestParameters.select !== undefined) {
            queryParameters['select'] = requestParameters.select;
        }

        if (requestParameters.order !== undefined) {
            queryParameters['order'] = requestParameters.order;
        }

        if (requestParameters.offset !== undefined) {
            queryParameters['offset'] = requestParameters.offset;
        }

        if (requestParameters.limit !== undefined) {
            queryParameters['limit'] = requestParameters.limit;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        if (requestParameters.range !== undefined && requestParameters.range !== null) {
            headerParameters['Range'] = String(requestParameters.range);
        }

        if (requestParameters.rangeUnit !== undefined && requestParameters.rangeUnit !== null) {
            headerParameters['Range-Unit'] = String(requestParameters.rangeUnit);
        }

        if (requestParameters.prefer !== undefined && requestParameters.prefer !== null) {
            headerParameters['Prefer'] = String(requestParameters.prefer);
        }

        const response = await this.request({
            path: `/feeds`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(FeedsFromJSON));
    }

    /**
     */
    async feedsGet(requestParameters: FeedsGetRequest): Promise<Array<Feeds>> {
        const response = await this.feedsGetRaw(requestParameters);
        return await response.value();
    }

    /**
     */
    async feedsPatchRaw(requestParameters: FeedsPatchRequest): Promise<runtime.ApiResponse<void>> {
        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.id !== undefined) {
            queryParameters['id'] = requestParameters.id;
        }

        if (requestParameters.name !== undefined) {
            queryParameters['name'] = requestParameters.name;
        }

        if (requestParameters.url !== undefined) {
            queryParameters['url'] = requestParameters.url;
        }

        if (requestParameters.priority !== undefined) {
            queryParameters['priority'] = requestParameters.priority;
        }

        if (requestParameters.hidden !== undefined) {
            queryParameters['hidden'] = requestParameters.hidden;
        }

        if (requestParameters.createdAt !== undefined) {
            queryParameters['created_at'] = requestParameters.createdAt;
        }

        if (requestParameters.updatedAt !== undefined) {
            queryParameters['updated_at'] = requestParameters.updatedAt;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (requestParameters.prefer !== undefined && requestParameters.prefer !== null) {
            headerParameters['Prefer'] = String(requestParameters.prefer);
        }

        const response = await this.request({
            path: `/feeds`,
            method: 'PATCH',
            headers: headerParameters,
            query: queryParameters,
            body: FeedsToJSON(requestParameters.feeds),
        });

        return new runtime.VoidApiResponse(response);
    }

    /**
     */
    async feedsPatch(requestParameters: FeedsPatchRequest): Promise<void> {
        await this.feedsPatchRaw(requestParameters);
    }

    /**
     */
    async feedsPostRaw(requestParameters: FeedsPostRequest): Promise<runtime.ApiResponse<void>> {
        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.select !== undefined) {
            queryParameters['select'] = requestParameters.select;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (requestParameters.prefer !== undefined && requestParameters.prefer !== null) {
            headerParameters['Prefer'] = String(requestParameters.prefer);
        }

        const response = await this.request({
            path: `/feeds`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: FeedsToJSON(requestParameters.feeds),
        });

        return new runtime.VoidApiResponse(response);
    }

    /**
     */
    async feedsPost(requestParameters: FeedsPostRequest): Promise<void> {
        await this.feedsPostRaw(requestParameters);
    }

}

/**
    * @export
    * @enum {string}
    */
export enum FeedsDeletePreferEnum {
    Representation = 'return=representation',
    Minimal = 'return=minimal',
    None = 'return=none'
}
/**
    * @export
    * @enum {string}
    */
export enum FeedsGetPreferEnum {
    Countnone = 'count=none'
}
/**
    * @export
    * @enum {string}
    */
export enum FeedsPatchPreferEnum {
    Representation = 'return=representation',
    Minimal = 'return=minimal',
    None = 'return=none'
}
/**
    * @export
    * @enum {string}
    */
export enum FeedsPostPreferEnum {
    Representation = 'return=representation',
    Minimal = 'return=minimal',
    None = 'return=none'
}
