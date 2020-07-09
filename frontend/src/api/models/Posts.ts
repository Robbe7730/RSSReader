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

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface Posts
 */
export interface Posts {
    /**
     * Note:
     * This is a Primary Key.<pk/>
     * @type {number}
     * @memberof Posts
     */
    id: number;
    /**
     * 
     * @type {string}
     * @memberof Posts
     */
    title: string;
    /**
     * 
     * @type {string}
     * @memberof Posts
     */
    description: string;
    /**
     * Note:
     * This is a Foreign Key to `feeds.id`.<fk table='feeds' column='id'/>
     * @type {number}
     * @memberof Posts
     */
    feedId: number;
    /**
     * 
     * @type {string}
     * @memberof Posts
     */
    link?: string;
    /**
     * 
     * @type {boolean}
     * @memberof Posts
     */
    read: boolean;
}

export function PostsFromJSON(json: any): Posts {
    return PostsFromJSONTyped(json, false);
}

export function PostsFromJSONTyped(json: any, ignoreDiscriminator: boolean): Posts {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': json['id'],
        'title': json['title'],
        'description': json['description'],
        'feedId': json['feed_id'],
        'link': !exists(json, 'link') ? undefined : json['link'],
        'read': json['read'],
    };
}

export function PostsToJSON(value?: Posts | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'title': value.title,
        'description': value.description,
        'feed_id': value.feedId,
        'link': value.link,
        'read': value.read,
    };
}

